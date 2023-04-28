from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from settings import TELEGRAM_CHAT_IDS

class IsAllowedUser(BoundFilter):
    async def check(self, message: Message):
        return message.from_user.id in TELEGRAM_CHAT_IDS
