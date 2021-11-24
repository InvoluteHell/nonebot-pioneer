from nonebot.adapters import Bot, Event
from nonebot.matcher import Matcher
from nonebot.plugin import on_command, on_message
from tools import run_plugin_main


class Recorder:
    def __init__(self, name: str, version: str):
        self.version = version
        self.name = name

    def list_all(self, id: str):
        pass


recorder = Recorder("Android", "0.0.2")


@run_plugin_main
def main():
    @on_command(("recorder", "version")).handle()
    async def handle_version(bot: Bot):
        await Matcher.finish(recorder.version)

    @on_command(("recorder", "name")).handle()
    async def handle_name(bot: Bot):
        await Matcher.finish(recorder.name)

    @on_message().handle()
    async def record_message(bot: Bot, event: Event):
        print(event.get_type())
        print(event.get_message())
