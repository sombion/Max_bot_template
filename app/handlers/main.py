from loguru import logger
from maxapi import Router, F
from maxapi.types import MessageCreated, MessageCallback
from maxapi.context import MemoryContext

router = Router()


@router.message_created(F.message.body.text)
async def agent(event: MessageCreated):
    logger.info(
        f"Пользователь: {event.from_user.user_id} написал: {event.message.body.text}"
    )
    await event.message.answer(text="Ответ на сообщение пользователя")


@router.message_callback(F.callback.payload == "btn_1")
async def exit_agent(callback: MessageCallback, context: MemoryContext):
    logger.info(f"Пользователь нажал кнопку 1")
    await callback.bot.send_message(
        chat_id=callback.chat.chat_id, text="Пользователь нажал кнопку 1"
    )


@router.message_callback(F.callback.payload == "btn_2")
async def exit_agent(callback: MessageCallback, context: MemoryContext):
    logger.info(f"Пользователь нажал кнопку 2")
    await callback.bot.send_message(
        chat_id=callback.chat.chat_id, text="Пользователь нажал кнопку 2"
    )
