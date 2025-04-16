from core import slow_print

Weight = 1

def run(player):
    slow_print("A lonely well sits in a clearing. A rope hangs into it.")

    choice = input("Climb down the well? (yes/no): ").strip().lower()
    if choice == "yes":
        slow_print("You climb down and discover a dusty backpack.")
        player.add_item("backpack")
    else:
        slow_print("You leave the well behind.")
