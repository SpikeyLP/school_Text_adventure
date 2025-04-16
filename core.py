import time
import sys

def slow_print(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Player:
    def __init__(self, name, health=100, inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.health = health
        self.inventory = inventory
    
    def add_item(self, item):
        self.inventory.append(item)
        slow_print("you got a "+ item)
        
    def __str__(self):
        return f"{self.name} (Health: {self.health}, Inventory: {self.inventory})"
    
    def change_Health(self,amount):
        self.health = self.health + amount
        if amount > 0 :
            slow_print("you gained "+str(amount)+" health")
        else :
            slow_print("you Lost "+str(abs(amount))+" health")
        slow_print("you now have "+str(self.health)+ " Health")