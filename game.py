from goblin import Goblin


ARENA_NAME = "Scary Larry's Domain"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The door to Larry's mom's basement creaks open, and a foul stench fills the air.")

    goblin = Goblin("Scary Larry")

    print(f"{goblin.name} is rotting on his computer with {goblin.health} health, and he lowk stanky.")
    goblin2=Goblin("Scary Le Terry")
    print(f"{goblin2.name} is rotting on his phone with {goblin2.health} health, and he smells bad.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
