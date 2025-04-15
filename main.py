import Scenes

def main():
    from core import Player, slow_print

    player = Player("Spike")
    slow_print("Welcome to the adventure.")

    # Call any scene like this:
    Scenes.scene_start.run(player)

if __name__ == "__main__":
    main()
