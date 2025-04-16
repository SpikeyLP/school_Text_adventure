from core import slow_print

Weight = 1

def run(player):
    slow_print("You spot a hatch covered in leaves.")

    if "knife" in player.inventory:
        slow_print("You use your knife to pry it open.")

    slow_print("1) Ignore it")
    slow_print("2) Try to open it")

    choice = input("> ").strip()

    if choice == "2":
        if "knife" in player.inventory:
            slow_print("Inside you find a map wrapped in oilskin.")
            player.add_item("map")
        else:
            slow_print("You try but can't open it barehanded.")
    elif choice == "1":
        slow_print("You walk away.")
