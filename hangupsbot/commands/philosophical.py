import asyncio, random

from hangups import hangouts_pb2

from hangupsbot.utils import strip_quotes, text_to_segments
from hangupsbot.commands import command

@command.register
def spaces_or_tabs(bot, event, *args):

    yield from event.conv.send_message(text_to_segments("Of course it's tabs! Who is their right mind uses spaces?"))
