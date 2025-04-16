from core import slow_print

Weight = 1

def run(player):
    slow_print("You arrive at a fast-moving river. A rickety bridge crosses it.")
    
    if "rope" in player.inventory:
        slow_print("You remember the rope in your bag. Might help if the bridge fails.")
    
    slow_print("What do you do?")
    slow_print("1) Cross the bridge")
    slow_print("2) Look for another path")
    
    if "rope" in player.inventory:
        slow_print("3) Tie the rope to yourself and cross carefully")
    
    choice = input("> ").strip()
    
    if choice == "1":
        slow_print("Halfway through, the bridge collapses!")
        player.change_Health(-20)
    elif choice == "2":
        slow_print("You spend hours but find a shallow spot to cross safely.")
    elif choice == "3" and "rope" in player.inventory:
        slow_print("The bridge breaks, but the rope saves you from the fall.")
        slow_print("You climb back and continue your journey.")
    else:
        slow_print("You wait, hoping something changes.")
