from core import slow_print

Weight = 1

def run(player):
    slow_print("You find a rusted chest half-buried in the ground.")

    if "knife" in player.inventory:
        slow_print("You could use your knife to break the latch.")

    slow_print("1) Walk away")
    slow_print("2) Try to open it")

    if "knife" in player.inventory:
        slow_print("3) Use knife to pry it open")

    choice = input("> ").strip()

    if choice == "3" and "knife" in player.inventory:
        slow_print("You break it open and find a strange potion.")
        player.add_item("healing potion")
    elif choice == "2":
        slow_print("You try but fail to open it.")
    else:
        slow_print("You move on.")
