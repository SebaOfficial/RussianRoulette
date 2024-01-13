import sys
import os
import signal
import shutil

class Terminal:
    def __init__(self, min_width: int, min_height: int) -> None:
        self.min_width = min_width
        self.min_height = min_height
        signal.signal(signal.SIGWINCH, self.check_screen_size)

    def get_size(self):
        return shutil.get_terminal_size()

    def check_screen_size(self) -> None:
        rows, columns = self.get_size()

        if rows < self.min_height or columns < self.min_width:
            print(f"Please make sure your terminal size is at least {self.min_width}x{self.min_height}")
            print(f"Your's {columns}x{rows}")
            sys.exit(1)

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
