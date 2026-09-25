import random
from goblin import Goblin
from hero import Hero
from random import randint
from enemy import Enemy
from boss import Boss


ARENA_NAME = "Scary Larry's Domain"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The door to Larry's mom's basement creaks open, and a foul stench fills the air.")

    hero=Hero("Spooky Rye")
    goblin = Goblin("Scary Larry")

    print(f"{goblin.name} is rotting on his computer with {goblin.health} health, and he lowk stanky.")
    goblin2=Goblin("Scary Le Terry")
    print(f"{goblin2.name} is rotting on his phone with {goblin2.health} health, and he smells bad.")
    print(f"{hero.name} is tuffy mcgee and is here to defeat le scary family with {hero.health} health.")
    teddy=Hero("Teddy")
    herodamage=hero.attack()
    herocritical_hit=random.randint(1, 100)
    if herocritical_hit<=1:
        print(f"{hero.name} does a critical stanky strike!")
        herodamage=hero.attack()+50
    goblin.take_damage(herodamage)
    if goblin.health <= 0:
        print(f"{goblin.name} has been defeated by {hero.name}!")
    else:
        goblindamage=goblin.attack()
        gobcritical_hit=random.randint(1, 100)
        if gobcritical_hit<=1:
                print(f"{goblin.name} does a critical stanky strike!")
                goblindamage=goblin.attack()+40
        hero.take_damage(goblindamage)

        bossguy=Boss("Scary Larry's Dad")
        




if __name__ == "__main__":
    main()
