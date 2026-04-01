import asyncio

from loguru import logger
from maxapi import Bot, Dispatcher

from app.config import settings
from app.handlers.main import router as main_router
from app.handlers.start import router as start_router


async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(start_router)
    dp.include_routers(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logger.info("Бот запущен")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот выключен")
