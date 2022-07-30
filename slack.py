import datetime
import pyautogui as gui
from random import randint
from time import sleep


POSITION_ONE = (153, 445)
POSITION_TWO = (153, 545)


def random_pause():
    seconds = randint(10, 30)
    print(f"Pausing for {seconds} seconds...")
    sleep(seconds)

minutes_to_run = False
start = datetime.datetime.now()

while not minutes_to_run:
    minutes_to_run = input("How many minutes would you like this to run for? ")
    if not minutes_to_run.isnumeric():
        print(f"Please enter an integer. '{minutes_to_run}' is not valid.")
        minutes_to_run=False

minutes_to_run = int(minutes_to_run)

gui.click(10, 10)

while datetime.datetime.now() < (start + datetime.timedelta(minutes=minutes_to_run)):
    gui.click(POSITION_ONE)
    random_pause()
    gui.click(POSITION_TWO)
    random_pause()

print(f"We have run for {minutes_to_run} minutes, ending now!")
