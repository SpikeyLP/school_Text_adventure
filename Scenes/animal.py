from core import slow_print

Weight = 1

def run(player):
    slow_print("As you walk along the forest, you spot a squirrel.")
    slow_print("The squirrel doesn't seem afraid of you.")

    choice = input("Do you approach the squirrel? (yes/no): ").strip().lower()

    if choice in ["yes", "y"]:
        slow_print("You slowly approach the squirrel.")
        slow_print("What do you do?")
        slow_print("1) Pet the squirrel")
        slow_print("2) Punch the squirrel")

        if "torch" in player.inventory:
            slow_print("3) Attack the squirrel with your torch")

        print()
        action = input("> ").strip()

        if action == "1":
            slow_print("The squirrel attacks you.")
            player.change_Health(-15)
        elif action == "2":
            slow_print("As you try to hit it, it attacks you.")
            player.change_Health(-25)
        elif action == "3" and "torch" in player.inventory:
            slow_print("You attack the squirrel with your torch.")
            slow_print("You successfully kill it and eat its meat.")
            player.change_Health(20)
        else:
            slow_print("You stand frozen, unsure what to do.")
    else:
        slow_print("You decide to leave the squirrel alone and continue on your path.")
