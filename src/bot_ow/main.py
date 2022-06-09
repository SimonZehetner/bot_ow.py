#!/usr/bin/env python
import logging
import os
import sys
from argparse import ArgumentParser, Namespace
from typing import Optional

from bot_ow.bot import DEFAULT_PREFIX, bot_ow

TOKEN_ENV_NAME = "DISCORD_TOKEN"


def _get_token(args: Namespace) -> Optional[str]:
    if args.token:
        return args.token
    token = os.getenv(TOKEN_ENV_NAME)
    if token:
        return token
    return None


def main() -> None:
    parser = ArgumentParser(
        description="Discord-Bot that adds '_ow'' to users nicknames",
    )
    parser.add_argument(
        "token",
        nargs="?",
        help=f"The Discord Token for this Bot. Alternatively, the `{TOKEN_ENV_NAME}`-environment variable can be used",
    )
    parser.add_argument(
        "--command-prefix",
        required=False,
        default=DEFAULT_PREFIX,
        help=f"The prefix for commands (default: `{DEFAULT_PREFIX}`)",
    )
    args = parser.parse_args()
    token = _get_token(args)
    if not token:
        parser.print_help()
        sys.exit(1)

    logging.basicConfig(
        filename="bot_ow.log",
        encoding="utf-8",
        level=logging.INFO,
        filemode="w",
        format="%(asctime)s:%(levelname)s:%(name)s: %(message)s",
    )
    logger = logging.getLogger("bot_ow.main")

    prefix: str = args.command_prefix
    if prefix != DEFAULT_PREFIX:
        logger.info(f"Changed command prefix to '{prefix}'")
        bot_ow.command_prefix = prefix
    bot_ow.run(token)


if __name__ == "__main__":
    main()
