from nonebot import on_command
from nonebot.adapters import Bot
from nonebot.matcher import Matcher


class TodoManager:
    def __init__(self):
        on_command(("todo", "list"), handlers=self.list_todos)

    def list_todos(self, bot: Bot, matcher: Matcher):
        pass
