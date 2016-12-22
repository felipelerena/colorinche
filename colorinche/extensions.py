from blessings import Terminal
from jinja2 import nodes
from jinja2.ext import Extension


class BlessingsExtension(Extension):
    tags = set(['bless'])

    def __init__(self, environment):
        super(BlessingsExtension, self).__init__(environment)
        self.term = Terminal()

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]
        body = parser.parse_statements(['name:end'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_render_blessings', args),
                               [], [], body).set_lineno(lineno)

    def _render_blessings(self, name, caller):
        bless_func = getattr(self.term, name)
        return bless_func(caller())
