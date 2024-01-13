import os
import argparse
from russian_roulette.core import RussianRoulette
from russian_roulette.utils import Terminal

def main():
    parser = argparse.ArgumentParser(description='Russian roulette game in your terminal.')
    parser.add_argument('--safe', action='store_true', help='run the game in safe mode')
    args = parser.parse_args()

    try:
        roulette = RussianRoulette(args.safe)

        width, height = roulette.get_revolver_size()
        terminal = Terminal(width, height)
        terminal.check_screen_size()

        roulette.disclaimer()
        roulette.play()

    except KeyboardInterrupt:
        print("")
        roulette.exit()

    print(f"{os.path.expanduser('~')}, {os.path.exists('/.dockerenv')}")


if __name__ == "__main__":
    main()
