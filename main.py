# main.py

import random
import Scenes
import Scenes._End
from core import Player,slow_print  # Import the Player class

def run_game():
    # Create the player object
    slow_print(r"Disclaimer: When tiping Anything other than the displayed options it will count as doing nothing")
    slow_print("What Is your name dear Traveler")
    name = input()
    
    player = Player(name)  # You can set the name or pass other attributes
    print()
    # Start with the start scene
    Scenes._start.run(player)
    print()
    Weights = []


    # Loop through the scenes and create the weighted list
    for scene_name, scene_module in Scenes.scene_modules.items():
        weight = getattr(scene_module, "Weight", 1)

        for _ in range(weight):
            Weights.append(scene_name)

    # Number of random scenes to pick
    x = 10  # Change this value to however many random scenes you want to run

    # Choose a random scene x times and run them
    for _ in range(x):
        random_scene = random.choice(Weights)
        Scenes.scene_modules[random_scene].run(player)
        Weights.remove(random_scene)
        print()

    Scenes._End.run(player)

if __name__ == "__main__":
    run_game()
