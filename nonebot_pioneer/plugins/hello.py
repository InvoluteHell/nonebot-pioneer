from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State

version = on_command("hello", rule=to_me(), priority=5)


@version.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await version.finish("hello")
