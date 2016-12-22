#! /usr/bin/env python3
from jinja2 import Environment, FileSystemLoader

from colorinche.extensions import BlessingsExtension


_env = None


def set_env(path):
    global _env
    _env = Environment(loader=FileSystemLoader(path),
                       extensions=[BlessingsExtension],
                       trim_blocks=True,
                       lstrip_blocks=True)

def print_template(name, template_data):
    template = _env.get_template(name)
    rendered = template.render(template_data)
    print(rendered)
