from core import slow_print

Weight = 0


def run(player):
    slow_print("You awaken in a dark forest. The air is damp and cold.")
    slow_print("There is a path leading north.")

    choice = input("Do you follow the path? (yes/no): ").strip().lower()
    
    if choice == "yes" or choice =="y":
        slow_print("You start walking cautiously along the path...")
        # You could now load scene_forest.py or another
    else:
        slow_print("You stay put, hearing distant howls. You might regret this...")