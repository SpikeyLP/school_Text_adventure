from core import slow_print

Weight = 1

def run(player):
    slow_print("You find a broken merchant wagon with crates spilled around.")

    choice = input("Do you search the crates? (yes/no): ").strip().lower()

    if choice in ["yes", "y"]:
        slow_print("You find a small vial labeled 'Antidote'.")
        player.add_item("antidote")
    else:
        slow_print("You leave the wreck untouched.")
