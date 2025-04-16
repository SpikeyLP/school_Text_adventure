from core import slow_print

Weight = 1

def run(player):
    slow_print("You find a cave entrance hidden behind some vines.")
    slow_print("It's pitch black inside. You can't see a thing.")

    if "torch" not in player.inventory:
        slow_print("You see something glinting nearby.")
        choice = input("Do you pick up the torch? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            player.add_item("torch")
        else:
            slow_print("You leave it. The darkness stays thick.")

    slow_print("What do you do?")
    slow_print("1) Enter the cave")
    slow_print("2) Walk away")

    if "torch" in player.inventory:
        slow_print("3) Light the torch and enter carefully")

    print()
    action = input("> ").strip()

    if action == "1":
        slow_print("You stumble blindly into the darkness and trip over a rock.")
        player.change_Health(-15)
    elif action == "2":
        slow_print("You leave the cave behind. Maybe next time.")
    elif action == "3" and "torch" in player.inventory:
        slow_print("You light the torch. The cave glows with flickering light.")
        slow_print("Inside, you find ancient carvings on the walls...")
        player.add_item("knowledge")
        slow_print("You quickly leave the cave and walk further.")
    else:
        slow_print("You're unsure and just head out.")
