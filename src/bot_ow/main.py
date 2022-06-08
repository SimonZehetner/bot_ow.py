#!/usr/bin/env python
import logging
import os

from bot_ow.bot import bot_ow

TOKEN_ENV_NAME = "DISCORD_TOKEN"


def _get_token() -> str:
    token = os.getenv(TOKEN_ENV_NAME)
    if not token:
        raise EnvironmentError(
            f"No Token provided! Please set the '{TOKEN_ENV_NAME}' environment variable."
        )
    return token


def main() -> None:
    logging.basicConfig(
        filename="bot_ow.log",
        encoding="utf-8",
        level=logging.INFO,
        filemode="w",
        format="%(asctime)s:%(levelname)s:%(name)s: %(message)s",
    )
    bot_ow.run(_get_token())


if __name__ == "__main__":
    main()
