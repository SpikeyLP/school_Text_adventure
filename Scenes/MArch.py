from core import slow_print

Weight = 1

def run(player):
    slow_print("The fog rolls in thick as you enter a marshy area.")
    slow_print("You hear whispering voices but can’t see anything.")

    choice = input("Do you keep going? (yes/no): ").strip().lower()

    if choice in ["yes", "y"]:
        slow_print("The fog parts, and a shimmering object catches your eye.")
        player.add_item("lucky charm")
    else:
        slow_print("You quickly turn around and leave the eerie marsh.")
