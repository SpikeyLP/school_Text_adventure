from core import slow_print

Weight = 1

def run(player):
    slow_print("As you enter a narrow corridor, a click echoes—an arrow trap!")

    if "shield" in player.inventory:
        slow_print("You raise your shield!")

    slow_print("1) Duck and roll")
    if "shield" in player.inventory:
        slow_print("2) Block with shield")

    choice = input("> ").strip()

    if choice == "1":
        slow_print("You mostly dodge, but get grazed.")
        player.change_Health(-5)
    elif choice == "2" and "shield" in player.inventory:
        slow_print("The arrow bounces off your shield harmlessly.")
    else:
        slow_print("The arrow strikes you.")
        player.change_Health(-15)
