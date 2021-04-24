

from adventuretutorial.game import check_for_save
import pathlib as Path
import adventuretutorial
from typing import Union
import time
from signalinterface import receive_msg
from signalinterface import send_msg



def main():


    while (True):

        player_id, message= receive_msg()
        # if Path("saved_player_{}.p".format(player_id)).is_file() and Path("saved_world_{}.p".format(player_id)).is_file():

        check_for_save(player_id,message)

        time.sleep(1)

if __name__ == "__main__":
    main()
