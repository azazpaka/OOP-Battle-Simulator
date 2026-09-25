import random
from enemy import Enemy


class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=250, attackPower=25)

    def attack(self):
        attackstyle= random.randint(1,2)
        if attackstyle==1:
            print("fireball brah")
            return random.randint(1, 10)
        else:
            print("big stanky strike")
            return self.attack_power()* random.randint(1, 2)
    def take_damage(self, damage):
        damage=damage*.75
        super().take_damage(damage)

    def stealDignity(self, hero):
        """steal dignity"""""
        self.dignity=self.dignity+hero.dignity
        hero.dignity=0
        print("hahaha i stole your dignity get owned and pwned")