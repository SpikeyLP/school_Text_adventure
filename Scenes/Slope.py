from core import slow_print

Weight = 1

def run(player):
    slow_print("You come across a steep rocky slope.")

    if "rope" in player.inventory:
        slow_print("You could use your rope to climb safely.")

    slow_print("1) Climb it")
    if "rope" in player.inventory:
        slow_print("2) Use the rope to climb")

    choice = input("> ").strip()

    if choice == "1":
        slow_print("You slip and hurt yourself.")
        player.change_Health(-20)
    elif choice == "2" and "rope" in player.inventory:
        slow_print("You tie the rope and climb without issue.")
    else:
        slow_print("You hesitate and look for another way.")
