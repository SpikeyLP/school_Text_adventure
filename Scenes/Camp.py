from core import slow_print

Weight = 1

def run(player):
    slow_print("You stumble on old campfire ashes.")
    slow_print("Something shiny sticks out of the soot.")

    choice = input("Do you dig through it? (yes/no): ").strip().lower()

    if choice == "yes" or choice == "y":
        slow_print("You find a silver ring.")
        player.add_item("silver ring")
    else:
        slow_print("You move on.")
