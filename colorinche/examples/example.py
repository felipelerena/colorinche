#! /usr/bin/env python3
from colorinche import print_template, set_env

def main():
    set_env()
    template = "menu.j2"

    opciones = [
        [1, "uno"],
        [2, "dos"],
        [3, "tres"]
    ]

    data = {
        "titulo": "Hola",
        "opciones": opciones,
    }
    print_template(template, data)


if __name__ == '__main__':
    main()
