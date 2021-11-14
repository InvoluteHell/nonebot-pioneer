from nonebot.adapters import Bot
from nonebot.matcher import Matcher
from nonebot.plugin import on_command


class Android:
    def __init__(self, name: str):
        self.version = "0.0.1"
        self.name = name

    def listen(self):
        on_command("version", handlers=[self.handle_version])
        on_command("name", handlers=[self.handle_name])

    async def handle_version(self, bot: Bot, matcher: Matcher):
        await matcher.finish(self.version)

    async def handle_name(self, bot: Bot, matcher: Matcher):
        await matcher.finish(self.name)
