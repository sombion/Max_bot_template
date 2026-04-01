from loguru import logger
from maxapi import Router
from maxapi.types import MessageCreated, CommandStart

from app.keyboards.main import create_start_btn


router = Router()


@router.bot_started()
async def get_bot_start(event: MessageCreated):
    logger.info(f"Пользователь запустил бота")
    start_text = "Пользователь запустил бота"
    kb = await create_start_btn()
    await event.bot.send_message(
        chat_id=event.chat.chat_id, text=start_text, attachments=[kb]
    )


@router.message_created(CommandStart())
async def get_start(event: MessageCreated):
    logger.info(f"Пользователь: {event.from_user.user_id} ввел команду /start")
    start_text = "Пользователь запустил бота"
    kb = await create_start_btn()
    await event.message.answer(start_text, attachments=[kb])
