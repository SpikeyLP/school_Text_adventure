from core import slow_print

def run(player):
    slow_print("You find a cave entrance hidden behind some vines.")
    slow_print("It's pitch black inside. You can't see a thing.")

    if "torch" not in player.inventory:
        slow_print("You see something glinting nearby.")
        choice = input("Do you pick up the torch? (yes/no): ").strip().lower()
        if choice == "yes":
            player.add_item("torch")
        else:
            slow_print("You leave it. The darkness stays thick.")
    
    slow_print("What do you do?")
    slow_print("1) Enter the cave")
    slow_print("2) Walk away")

    if "torch" in player.inventory:
        slow_print("3) Light the torch and enter carefully")

    choice = input("> ").strip()

    if choice == "1":
        slow_print("You stumble blindly into the darkness and trip over a rock.")
        player.take_damage(15)
    elif choice == "2":
        slow_print("You leave the cave behind. Maybe next time.")
    elif choice == "3" and "torch" in player.inventory:
        slow_print("You light the torch. The cave glows with flickering light.")
        slow_print("Inside, you find ancient carvings on the walls...")
        player.add_item("mysterious rune")
    else:
        slow_print("You stand frozen, unsure what to do.")

