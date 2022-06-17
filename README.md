# Bot_OW
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Stupid Discord-Bot, that adds `_ow` to new members nicknames.
Used in [Cicero's University](https://discord.gg/Fj7yUqF)


## Install
### Build-Dependencies
* Python >=3.7
* [poetry](https://github.com/python-poetry/poetry)

### Run
```bash
# 1. Clone the repo
git clone git@github.com:SimonZehetner/bot_ow.py.git && cd bot_ow.py
# 2. Install dependencies
poetry install
# 3. Activate the venv
source .venv/bin/activate
# 4. Provide the discord token and run the Bot
bot_ow "<your_token_goes_here>" &
```
Alternatively, you can specify the `DISCORD_TOKEN` environment variable
## Usage
When a new member joins the server, `_ow` is appended to their nickname. The users can change their nickname back.

### Commands
#### `!overwatching`
Appends `_ow` to all members of the server (if not already ends with `_ow`). Can be used for initial setup of the server.

> Only users with the `Manage Nicknames`-permission are allowed to execute this command!
