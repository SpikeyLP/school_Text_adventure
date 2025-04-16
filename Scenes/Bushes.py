from core import slow_print

Weight = 1

def run(player):
    slow_print("You hear rustling in the bushes followed by a howl.")
    slow_print("Something leaps at you!")

    if "knife" in player.inventory:
        slow_print("You quickly draw your knife.")

    slow_print("1) Run")
    slow_print("2) Fight back")

    if "knife" in player.inventory:
        slow_print("3) Stab the creature")

    choice = input("> ").strip()

    if choice == "1":
        slow_print("You get away but not unscathed.")
        player.change_Health(-10)
    elif choice == "2":
        slow_print("You fight with bare hands and win, barely.")
        player.change_Health(-25)
    elif choice == "3" and "knife" in player.inventory:
        slow_print("You stab it. It screeches and flees.")
        player.change_Health(10)
    else:
        slow_print("It knocks you down before vanishing.")
        player.change_Health(-15)
