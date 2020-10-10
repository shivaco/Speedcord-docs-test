"""
Created by Epic at 9/24/20
"""
from speedcord.http import Route


class BaseContext:
    def __init__(self, client, data):
        """
        Basic context, use one of the subclasses for typing
        :param client: the client
        """
        self.client = client
        self.data = data

        # This possibly sucks performance wise? Please make a pr if there is a better way to do this.
        for field, field_data in data.items():
            setattr(self, field, field_data)


class MessageContext(BaseContext):
    """
    Message context

    Autogenerated by BaseContext
    """
    id = None
    channel_id = None
    guild_id = None
    author = None
    member = None
    content = None
    timestamp = None
    edited_timestamp = None
    tts = None
    mention_everyone = None
    mentions = None
    mention_roles = None
    mention_channels = None
    attachments = None
    embeds = None
    reactions = None
    nonce = None
    pinned = None
    webhook_id = None
    type = None
    activity = None
    application = None
    message_reference = None
    flags = None

    async def send(self, **kwargs):
        route = Route("POST", "/channels/{channel_id}/messages", channel_id=self.channel_id)
        return await self.client.http.request(route, json=kwargs)
