from core import slow_print

Weight = 1

def run(player):
    slow_print("High up in a tree you spot a large bird nest.")
    if "rope" in player.inventory:
        slow_print("You could use your rope to climb.")

    choice = input("Climb up? (yes/no): ").strip().lower()
    if choice == "yes":
        if "rope" in player.inventory:
            slow_print("You climb the tree and find a feather in the nest.")
            player.add_item("feather")
        else:
            slow_print("You cannot climb without a rope.")
    else:
        slow_print("You leave the tree behind.")
