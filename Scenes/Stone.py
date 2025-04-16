from core import slow_print

Weight = 1

def run(player):
    slow_print("You find a cracked stone with something wedged inside.")

    if "glowing stone" in player.inventory:
        slow_print("The glowing stone reacts—buzzing faintly.")

    slow_print("What do you do?")
    slow_print("1) Leave it")
    slow_print("2) Smash it open")

    choice = input("> ").strip()

    if choice == "2":
        slow_print("You smash it and find a small knife inside.")
        player.add_item("knife")
    elif choice == "1":
        slow_print("You decide to leave it alone.")
    else:
        slow_print("Nothing happens.")
