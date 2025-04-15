import time
import sys

# Slow-printing text like a real text adventure
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        slow_print(f"> You picked up: {item}")

    def take_damage(self, amount):
        self.health -= amount
        slow_print(f"> You took {amount} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
