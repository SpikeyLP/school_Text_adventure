from core import slow_print

Weight = 1

def run(player):
    slow_print("You find a small merchant stall with various goods.")
    slow_print("The merchant offers a strange-looking potion.")

    choice = input("Do you buy the potion? (yes/no): ").strip().lower()
    if choice in ["yes", "y"]:
        slow_print("You drink the potion, feeling revitalized!")
        player.add_item("antidote")
    else:
        slow_print("You leave the stall without buying anything.")
