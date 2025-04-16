from core import slow_print

Weight = 1

def run(player):
    slow_print("A thick fog covers the clearing. It's easy to get lost.")

    if "map" in player.inventory:
        slow_print("You check your map and find the safest path.")

    slow_print("1) Charge forward")
    if "map" in player.inventory:
        slow_print("2) Follow the route on your map")

    choice = input("> ").strip()

    if choice == "1":
        slow_print("You stumble into brambles.")
        player.change_Health(-10)
    elif choice == "2" and "map" in player.inventory:
        slow_print("You reach the other side unharmed.")
    else:
        slow_print("You wander until the fog lifts.")
