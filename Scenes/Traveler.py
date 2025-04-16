from core import slow_print

Weight = 1

def run(player):
    slow_print("A cloaked figure appears on the path.")
    slow_print('"Got anything to trade?" they ask.')

    if "torch" in player.inventory:
        slow_print('He eyes your torch. "That could be useful."')

    slow_print("What do you offer?")
    slow_print("1) Offer nothing")
    if "torch" in player.inventory:
        slow_print("2) Offer your torch")
    
    choice = input("> ").strip()
    
    if choice == "1":
        slow_print('"Suit yourself," he says and walks away.')
    elif choice == "2" and "torch" in player.inventory:
        slow_print("He hands you a glowing stone in return.")
        player.remove_item("torch")
        player.add_item("glowing stone")
    else:
        slow_print("You hesitate too long, and he's gone.")
