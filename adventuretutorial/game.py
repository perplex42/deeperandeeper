"""
A simple text adventure designed as a learning experience for new programmers.
"""
__author__ = 'Phillip Johnson'
import world
from player import Player
from pathlib import Path
import pickle
from signalinterface import receive_msg

def play(player_id, message, saved_world=None, saved_player=None):
    if saved_world and saved_player:
        world._world = saved_world
        player = saved_player
    else:
        world.load_tiles()
        player = Player()
    return game_loop(player, player_id, message)

def game_loop(player, player_id, message):
    answer_message = ''
    room = world.tile_exists(player.location_x, player.location_y)

    if player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:

            available_actions = room.available_actions()

            action_input = message
            correct_command = False
            for action in available_actions:
                if action.name == action_input or action.hotkey == action_input :
                    player.do_action(action, **action.kwargs)
                    correct_command=True
            if not correct_command:
                answer_message=answer_message+'\n'+room.intro_text()
                answer_message=answer_message+'\n'+"Choose an action:\n"
                for action in available_actions:
                    answer_message = answer_message +'\n'+ str(action)

        player.save_and_exit(player_id)
    print(answer_message)
    return answer_message


def check_for_save(player_id, message):
    if Path("saved_player_{}.p".format(player_id)).is_file() and Path("saved_world_{}.p".format(player_id)).is_file():
        saved_world = pickle.load(open("saved_world_{}.p".format(player_id), "rb"))
        saved_player = pickle.load(open("saved_player_{}.p".format(player_id), "rb"))
        return_message = play(player_id, message, saved_world, saved_player)
    else:
        return_message = play(player_id, message)
    return return_message

if __name__ == "__main__":
    check_for_save()
