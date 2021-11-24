from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.matcher import Matcher
from tools import run_plugin_main


@run_plugin_main
def main():
    @on_command(("todo", "version")).handle()
    async def list_todos(bot: Bot, event: Event, matcher: Matcher):
        print(event.get_user_id())
        await matcher.finish("todo version: 0.0.1")
