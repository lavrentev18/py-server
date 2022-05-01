import re
import config
from jinja2 import Environment, FileSystemLoader, select_autoescape

class View:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(config.TEMPLATES_DIR), autoescape=select_autoescape())

    def render(self, template, params=None):
        templateName = re.sub(r"\..*", "", template)

        compiled = self.env.get_template("{}{}".format(templateName, config.TEMPLATES_EXTENSION))
        return compiled.render(params)


templateEngine = View()
