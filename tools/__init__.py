"""
Tools for nonebot_pioneer
"""


import nonebot

tool_version = "0.0.1"
"""tool version"""


def bot_initialized():
    try:
        nonebot.get_driver()
        return True
    except ValueError:
        return False


def run_plugin_main(func):
    if bot_initialized():
        func()
    return func
