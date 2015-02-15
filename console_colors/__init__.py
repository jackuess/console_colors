from collections import namedtuple
import subprocess
import sys

Color = namedtuple("Color", ["fg", "bg"])

BLACK = Color(fg="\033[30m", bg="\033[40m")
RED = Color(fg="\033[31m", bg="\033[41m")
GREEN = Color(fg="\033[32m", bg="\033[42m")
YELLOW = Color(fg="\033[33m", bg="\033[43m")
BLUE = Color(fg="\033[34m", bg="\033[44m")
MAGENTA = Color(fg="\033[35m", bg="\033[45m")
CYAN = Color(fg="\033[36m", bg="\033[46m")
WHITE = Color(fg="\033[37m", bg="\033[47m")
INTENSE_BLACK = Color(fg="\033[90m", bg="\033[100m")
INTENSE_RED = Color(fg="\033[91m", bg="\033[101m")
INTENSE_GREEN = Color(fg="\033[92m", bg="\033[102m")
INTENSE_YELLOW = Color(fg="\033[93m", bg="\033[103m")
INTENSE_BLUE = Color(fg="\033[94m", bg="\033[104m")
INTENSE_MAGENTA = Color(fg="\033[95m", bg="\033[105m")
INTENSE_CYAN = Color(fg="\033[96m", bg="\033[106m")
INTENSE_WHITE = Color(fg="\033[97m", bg="\033[107m")
BLINK = "\033[5m"
RESET = "\033[0m"


def rgb(r, g, b):
    """Creates a custom XTerm RGB color, to be used as parameter to Foreground
    or Background."""
    return Color(fg="\033[38;2;{};{};{}m".format(r, g, b),
                 bg="\033[48;2;{};{};{}m".format(r, g, b))


class Blink(object):
    """Makes text in a terminal blink."""
    def __init__(self, f=sys.stdout):
        self.file = f
        self.modifier = BLINK

    def __enter__(self):
        self.file.write(self.modifier)
        self.file.flush()

    def __exit__(self, *args):
        self.file.write(RESET)
        self.file.flush()


class Foreground(Blink):
    """Makes text colored in a terminal"""
    def __init__(self, color, f=sys.stdout):
        self.modifier = color.fg
        self.file = f


class Background(Blink):
    """Makes the background of text colored in a terminal"""
    def __init__(self, color, f=sys.stdout):
        self.modifier = color.bg
        self.file = f


def print_using_font(string, font):
    try:
        subprocess.call(["toilet", "-f", font, string])
    except FileNotFoundError:
        raise RuntimeError("print_using_font requires toilet")
