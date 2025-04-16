import time
import sys

def slow_print(text, delay=0.03):
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
        
    def __str__(self):
        return f"{self.name} (Health: {self.health}, Inventory: {self.inventory})"
