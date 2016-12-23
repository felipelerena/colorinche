#! /usr/bin/env python3
from blessings import Terminal
from colorinche import print_template, set_env

def main():
    set_env()
    template = "menu.j2"
    term = Terminal()

    options = [
        [1, "First", "the first option"],
        [2, "Second", "the middle option"],
        [3, "Third", "the final option"]
    ]

    data = {
        "title": "Awesome Example",
        "options": options,
    }
    with term.fullscreen():
        print_template(template, data)
        input("Press Enter to close")


if __name__ == '__main__':
    main()
