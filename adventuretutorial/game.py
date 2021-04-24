"""
A simple text adventure designed as a learning experience for new programmers.
"""
__author__ = 'Phillip Johnson'
import world
from player import Player
from pathlib import Path
import pickle
from signalinterface import receive_msg
from signalinterface import send_msg


def play(player_id, message, saved_world=None, saved_player=None):
    if saved_world and saved_player:
        world._world = saved_world
        player = saved_player
    else:
        world.load_tiles()
        player = Player()
    game_loop(player, player_id, message)

def game_loop(player, player_id, message):
    room = world.tile_exists(player.location_x, player.location_y)
    send_msg(player_id, room.intro_text())
    if player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            send_msg(player_id, "Choose an action:\n")
            available_actions = room.available_actions()
            if message == '' :
                for action in available_actions:
                    send_msg(player_id, action)
            else:
                action_input = message
                print()
                for action in available_actions:
                    if action_input == action.hotkey:
                        player.do_action(action, **action.kwargs)
                        break
        player.save_and_exit(player_id)


def check_for_save(player_id, message):
    if Path("saved_player_{}.p".format(player_id)).is_file() and Path("saved_world_{}.p".format(player_id)).is_file():
        saved_world = pickle.load(open("saved_world_{}.p".format(player_id), "rb"))
        saved_player = pickle.load(open("saved_player_{}.p".format(player_id), "rb"))
        play(player_id, message, saved_world, saved_player)
    else:
        play(player_id, message)

if __name__ == "__main__":
    check_for_save()
