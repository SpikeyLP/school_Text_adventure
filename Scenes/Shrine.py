from core import slow_print

Weight = 1

def run(player):
    slow_print("You come across a small mossy shrine with an offering bowl.")
    choice = input("Do you place a coin in the bowl? (yes/no): ").strip().lower()

    if choice in ["yes", "y"]:
        slow_print("The shrine glows softly. A charm appears in the bowl.")
        player.add_item("lucky charm")
    else:
        slow_print("The shrine remains silent. You walk away.")
