import asyncio
import locale
from datetime import datetime

from src.main import bot, dp, redis
from src.router import main_router
from src.funcs import create_schedule

locale.setlocale(locale.LC_ALL, '')

dp.include_router(main_router)


async def main() -> None:
    await redis.set(name='RUB', value="1")
    await asyncio.create_task(create_schedule())
    await dp.start_polling(bot)


if __name__ == '__main__':
    print(f'Бот запущен ({datetime.now().strftime("%H:%M:%S %d.%m.%Y")}).')
    asyncio.run(main())
