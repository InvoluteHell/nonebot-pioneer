from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from tools import tool_version

version = on_command("version", rule=to_me(), priority=5)


@version.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await version.finish(tool_version)
