import asyncio
import logging

import discord.errors
from discord import Intents, Member, Permissions
from discord.ext.commands import Bot, Context

REQUIRED_PERMISSIONS = Permissions(manage_nicknames=True)
DEFAULT_PREFIX = "!"

logger = logging.getLogger(__name__)

_intents = Intents.default()
_intents.members = True
bot_ow = Bot(intents=_intents, command_prefix=DEFAULT_PREFIX)


@bot_ow.event
async def on_ready() -> None:
    logger.info("logged in")


@bot_ow.event
async def on_member_join(member: Member) -> None:
    logger.info(f"New member: {member}")
    await _rename_member(member)


@bot_ow.command(name="overwatching")
async def overwatching(ctx: Context) -> None:
    author: Member = ctx.author
    if author.top_role.permissions.is_superset(REQUIRED_PERMISSIONS):
        logger.info(f"User {author.display_name} is not permitted to manage nicknames")
        return
    tasks = map(_rename_member, ctx.guild.members)
    await asyncio.gather(*tasks)


async def _rename_member(member: Member) -> None:
    name: str = member.display_name
    if name.lower().endswith("_ow"):
        return
    changed_name = f"{name}_ow"
    try:
        await member.edit(nick=changed_name)
        logger.info(f"Renamed '{name}' to '{changed_name}'")
    except discord.errors.Forbidden:
        logger.warning(f"Failed to rename user '{name}'")
