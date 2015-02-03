import curses
from curses import wrapper as curses_wrapper

import json

# import facebook


class UI:
    def __init__(self):
        # Initialise curses screen
        self.stdscr = curses.initscr()
        # Disable echo of characters
        curses.noecho()
        # Remove need to press enter before reacting to key press
        curses.cbreak()
        # Process special characters
        self.stdscr.keypad(1)

        # Ensure terminal is cleaned up if program crashes in main_loop
        curses_wrapper(self.main_loop)

    def main_loop(self, stdscr):
        while True:
            pass
        exit()

    def exit(self):
        # Shut everything down nicely
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()


class Facbook:
    def __init__(self, token):
        self.token = token


class Application:
    def __init__(self, config):
        ui = UI()


# Argument to specify config file
CONFIG_ARG = "--config"

DEFAULT_CONFIG = {
    'config_location': "~/.config/fcli.conf"
    }

SHORT_NOTATION_ARGS = {
    'c': 'config'
    }


def config_file_to_dict(file_path):
    with open(file_path) as f:
        file_str = f.read()
        config_dict = json.loads(file_str)
        return config_dict


def main(*args):
    """
    Process arguments, read config file and start the application.
    Will require more error checking
    """
    config = DEFAULT_CONFIG.copy()
    while len(args) > 0:
        arg = args.pop()
        if arg[:2] == "--":
            arg = arg[2:]
        elif arg[0] == '-':
            try:
                arg = SHORT_NOTATION_ARGS[arg[1:]]
            except AttributeError:
                # Invalid argument. Die.
                pass
        # Import settings from config file if specified
        if arg == CONFIG_ARG:
            config['config_location'] = args.pop()
            config_file_dict = config_file_to_dict(config['config_location'])
            # Merge configs, with config in file taking priority over defaults
            config = dict(
                list(config.items()) + list(config_file_dict.items()))
        else:
            config[arg] = args.pop()
    Application(config)


if __name__ == "__main__":
    main()
