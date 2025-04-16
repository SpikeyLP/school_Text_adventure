from core import slow_print
from time import sleep

Weight = 0

 
def run(player):
    slow_print("A Little Girl appears in a Clearing")
    slow_print("What do you do?")
    
    slow_print("1) approach her")
    slow_print("2) Run Away")
    choice = input("> ").strip()
    if choice == "1":
        slow_print("the Little Girl turns out to be a mimic and kill you ;(")
        slow_print("GAMEOVER", delay=0.2)
        sleep(.5)
        quit

    elif choice == "2":
        slow_print("the Little Girl runs after you and catches you by surprise and kills you she was a Mimic")
        slow_print("GAMEOVER", delay=0.2)
        sleep(.5)
        quit