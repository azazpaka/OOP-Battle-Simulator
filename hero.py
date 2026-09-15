import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 15
    def attack(self):
        return random.randint(self.attack_power, 25)
    def take_damage(self, damage):
         self.health = max(0, self.health - damage)
         print(f"{self.name} takes {damage} damage, his health is now {self.health}.")
    def is_alive(self):
        if self.health > 0:
            print (f"{self.name} is still alive with {self.health} health.")
        else: 
            print (f"{self.name} has been defeated.")