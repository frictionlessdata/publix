from ...plugin import Plugin


class TopicsPlugin(Plugin):
    priority = 70
    profile = {
        "type": "object",
        "properties": {
            "selector": {"type": "string"},
        },
    }

    @Plugin.property
    def selector(self):
        return self.config.get("selector", "h2, h3")

    # Process

    def process_markup(self, markup):
        if not self.config:
            return

        # Update markup
        markup.add_style("style.css")
        markup.add_script("https://unpkg.com/tocbot@4.12.3/dist/tocbot.min.js")
        markup.add_script("script.js", selector=self.selector)
        markup.add_markup(
            "markup.html",
            target="#livemark-left",
        )
