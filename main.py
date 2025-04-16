# main.py

import random
import Scenes
import Scenes.scene_start
from core import Player,slow_print  # Import the Player class

def run_game():
    # Create the player object
    slow_print("What Is your name dear Traveler")
    name = input()
    
    player = Player(name)  # You can set the name or pass other attributes

    # Start with the start scene
    Scenes.scene_start.run(player)
    
    Weights = []


    # Loop through the scenes and create the weighted list
    for scene_name, scene_module in Scenes.scene_modules.items():
        weight = getattr(scene_module, "Weight", 1)

        for _ in range(weight):
            Weights.append(scene_name)

    # Number of random scenes to pick
    x = 5  # Change this value to however many random scenes you want to run

    # Choose a random scene x times and run them
    for _ in range(x):
        random_scene = random.choice(Weights)
        Scenes.scene_modules[random_scene].run(player)

if __name__ == "__main__":
    run_game()
