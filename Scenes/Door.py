from core import slow_print

Weight = 1

def run(player):
    slow_print("You reach an old locked door embedded in stone.")

    if "ancient key" in player.inventory:
        slow_print("You pull out the key... it might fit.")

    slow_print("1) Kick the door")
    slow_print("2) Ignore it")
    if "ancient key" in player.inventory:
        slow_print("2) Use the ancient key")

    choice = input("> ").strip()

    if choice == "1":
        slow_print("You hurt your foot. It's solid stone.")
        player.change_Health(-5)
    elif choice == "2":
        slow_print("You ignore the door and walk along")
    elif choice == "3" and "ancient key" in player.inventory:
        slow_print("The key turns smoothly. The door opens into a secret room.")
        player.add_item("treasure")
    else:
        slow_print("Nothing happens.")
