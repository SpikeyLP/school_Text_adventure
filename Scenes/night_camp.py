from core import slow_print

Weight = 1

def run(player):
    slow_print("Night falls. You need to rest.")
    
    if "torch" in player.inventory:
        slow_print("You can light your torch to keep the beasts away.")
    
    slow_print("What do you do?")
    slow_print("1) Sleep without protection")
    slow_print("2) Stay awake all night")
    
    if "torch" in player.inventory:
        slow_print("3) Light your torch and sleep")
    
    choice = input("> ").strip()
    
    if choice == "1":
        slow_print("A creature sneaks up and scratches you.")
        player.change_Health(-10)
    elif choice == "2":
        slow_print("You stay safe but feel exhausted.")
        player.change_Health(-5)
    elif choice == "3" and "torch" in player.inventory:
        slow_print("The torch keeps danger at bay. You sleep well.")
        player.change_Health(10)
    else:
        slow_print("You stare at the stars, indecisive.")
