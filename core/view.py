from jinja2 import Environment, FileSystemLoader, select_autoescape
from config.views import TEMPLATES_DIR


class View:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=select_autoescape())

    def render(self, template, params=None):
        template = self.env.get_template(template)
        return template.render(params)


viewer = View()
