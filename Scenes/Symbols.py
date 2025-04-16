from core import slow_print

Weight = 1

def run(player):
    slow_print("You see glowing runes on a large stone slab.")

    if "glowing stone" in player.inventory:
        slow_print("The stone hums in sync with the glowing runes.")

    slow_print("1) Ignore them")
    if "glowing stone" in player.inventory:
        slow_print("2) Place the stone into the groove")

    choice = input("> ").strip()

    if choice == "2" and "glowing stone" in player.inventory:
        slow_print("The ground shifts. A secret path opens.")
        player.add_item("ancient key")
    else:
        slow_print("The runes stay silent.")
