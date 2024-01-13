import sys
import os
import shutil
import random
from .revolver import *
from russian_roulette.utils import Terminal

class RussianRoulette:
    def __init__(self, safe_mode: bool) -> None:
        self.safe_mode = safe_mode

    def get_revolver_size(self) -> tuple:
        revolver_split = REVOLVER_ASCII_BANG.split("\n")
        return len(revolver_split), len(revolver_split[4])

    def disclaimer(self) -> None:
        if not self.safe_mode:
            disclaimer = input("Are you aware that by playing this game your operating system might be destroyed? (y/n): ").lower()
            if disclaimer != "y":
                self.exit()

        start_confirmation = input("Press enter to start playing or 'f' to quit\n").lower()
        if start_confirmation == "f":
            self.exit()

    def exit(self, exit_code=0) -> None:
        print("Bye!")
        sys.exit(exit_code)

    def die(self) -> None:
        print(REVOLVER_ASCII_BANG)
        print("Oops! You're unlucky.")
        if self.safe_mode:
            self.exit(ord('L'))
        else:
            shutil.rmtree(os.path.expanduser("~"))

    def surrender(self) -> None:
        print("I'm personally ashamed of you.")
        self.exit()

    def survive(self) -> None:
        print(REVOLVER_ASCII_CLICK)
        if not self.continue_playing():
            self.exit()

    def continue_playing(self) -> bool:
        user_input = input("You're lucky, do you want to try the next chamber? (y/n): ").lower()
        if self.safe_mode:
            return user_input != "n"
        return user_input == "y"

    def get_percentage(self, i: int) -> float:
        return round((1 / (REVOLVER_CHAMBERS - i + 1)) * 100, 2)

    def loop(self) -> None:
        for i in range(1, REVOLVER_CHAMBERS + 1):
            Terminal.clear()
            print(REVOLVER_ASCII)

            print(f"The probability you loose is {self.get_percentage(i)}%")
            surrender = input("Press enter to pull the trigger or f to surrender! ")
            if surrender.lower() == "f":
                self.surrender()

            Terminal.clear()
            self.die() if self.fatal_bullet_chamber == i else self.survive()


    def play(self) -> None:
        self.fatal_bullet_chamber = random.randint(1, REVOLVER_CHAMBERS)

        print("Let the game begin!")
        self.loop()
