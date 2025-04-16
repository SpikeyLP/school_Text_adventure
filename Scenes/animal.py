from core import slow_print

Weight = 1

def run(player):
    slow_print("as you walk along the forest you spot a squirell")
    slow_print("you notice the squirell isnt afraid of you.")

    choice = input("Do you aprouch the squirell? (yes/no)").strip().lower()
    
    if choice == "yes" or choice =="y":
        slow_print("You start slowly aproaching the squirell")
        slow_print("What do you do?")
        slow_print("1) Pet The squirell")
        slow_print("2) Punch The squirell")
        
        if "torch" in player.inventory:
            slow_print("3) Atack the squirell with your torch")
            
        print()
        choice = input("> ").strip()
        if choice == "1":
            slow_print("The squirell Atacks you.")
            player.change_Health(-15)
        elif choice == "2":
            slow_print("As you try to hit it, it atacks you.")
            player.change_Health(-25)
        elif choice == "3" and "torch" in player.inventory:
            slow_print("You Atack the squirell with your torch")
            slow_print("You succesfully kill it and ate his meat")
            player.change_Health(20)
        else:
            slow_print("You stand frozen, unsure what to do.")

