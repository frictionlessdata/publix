import os
import inspect
import jsonschema
from jinja2 import Template
from .helpers import cached_property


class Plugin:
    profile = {}

    @cached_property
    def name(self):
        return self.__class__.__name__.replace("Plugin", "").lower()

    # Actions

    def validate_document(self, document):
        if self.profile:
            jsonschema.validate(document.config.get(self.name), self.profile)

    def prepare_document(self, document):
        pass

    def process_document(self, document):
        pass

    def cleanup_document(self, document):
        pass

    def process_snippet(self, snippet):
        pass

    def process_markup(self, markup):
        pass

    # Helpers

    def get_config(self, markup):
        return markup.document.config.get(self.name, {})

    def add_style(self, markup, *, path, to="head", **data):
        style = self.read_asset(path, tag="style", **data)
        markup.query(to).append(style)

    def add_script(self, markup, *, path, to="body", **data):
        script = self.read_asset(path, tag="script", **data)
        markup.query(to).append(script)

    def add_element(self, markup, *, path, to="body", **data):
        element = self.read_asset(path, **data)
        markup.query(to).append(element)

    def read_asset(self, *path, tag=None, **data):
        path = os.path.join(os.path.dirname(inspect.getfile(self.__class__)), *path)
        with open(path) as file:
            text = file.read()
        if tag:
            text = f"<{tag}>\n\n{text}\n</{tag}>\n"
        if data:
            template = Template(text)
            text = template.render(**data)
        return text
