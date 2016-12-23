#! /usr/bin/env python3
from jinja2 import Environment, FileSystemLoader

from colorinche.extensions import BlessingsExtension, LocationExtension


_env = None


def set_env(path=None):
    global _env

    if path is None:
        path = "templates"

    _env = Environment(loader=FileSystemLoader(path),
                       extensions=[BlessingsExtension, LocationExtension],
                       trim_blocks=True,
                       lstrip_blocks=True)

def print_template(name, template_data):
    template = _env.get_template(name)
    rendered = template.render(template_data)
    print(rendered)
