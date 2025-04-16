from core import slow_print

Weight = 1

def run(player):
    slow_print("In the middle of the path sits a stump with three colored stones.")
    slow_print("Red, blue, and green.")

    slow_print("Choose one to press:")
    slow_print("1) Red")
    slow_print("2) Blue")
    slow_print("3) Green")

    choice = input("> ").strip()

    if choice == "1":
        slow_print("The stump opens and reveals a fire crystal.")
        player.add_item("fire crystal")
    elif choice == "2":
        slow_print("You get sprayed by icy mist. Refreshing!")
        player.change_Health(5)
    elif choice == "3":
        slow_print("Thorns sprout and scratch you.")
        player.change_Health(-5)
    else:
        slow_print("You hesitate and nothing happens.")
