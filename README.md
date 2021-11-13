# nonebot-pioneer

This project is a playground for [NoneBot2][nonebot2]. Documents for NoneBot2 could be found [->here][nonebot2-message-matcher].


## Environment Requirements

- [poetry][poetry] >= 1.1

> Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

> Poetry install script: https://github.com/python-poetry/poetry/blob/master/install-poetry.py. To install Poetry, please run this file with a globally installed python interpreter.

## How to Start

1. Clone this repo and change working directory: `cd <folder>`.
2. Run `poetry install -no-root` to install dependencies except this "package". It will create a virtual environment under `./.venv/`.
3. Activate the virtual environment created at the previous step and run `nb run` to start the bot. Nonebot test frontend will be running at: http://localhost:8080/test/ .

> `nb` is a command from `nb-cli`, which is the cli for NoneBot2.


## Project Directory Structure and some Files

### `./nonebot_pioneer/plugins`
This directory is used for local plugins. Evary pyhon module (single file or folder module) will be loaded as plugin.

### `./tools`
The tools package for this project, which should be imported by like `from tools import xxx`.

### `./poetry.toml`
Configuration for Poetry.

### `./pyproject.toml`
"Package" information for this project. Poetry will use this file to install packages and `./bot.py` will load plugins accordingly as well.

## Special Settings for Visual Studio Code.
Please install all extensions recommended by this project (via `./.vscode/extensions.json`).

### Linting
Linting is enabled and engine [flake8] is token with default settings.

### Formatting
Formatter [black] is selected with some configurations in `./pyproject.toml`.

### Debugging
A launch configuration is add to this project, please use the default debugger.

## Some Notes:
Dockerfile has not been edited correctly, some modification may needed.



[poetry]:https://python-poetry.org/docs/
[nonebot2]:https://v2.nonebot.dev/
[nonebot2-message-matcher]:https://v2.nonebot.dev/guide/creating-a-matcher.html
[flake8]:https://flake8.pycqa.org/en/latest/
[black]:https://black.readthedocs.io/en/stable/index.html