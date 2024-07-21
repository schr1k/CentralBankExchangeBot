import xmltodict
from aiogram.client.session import aiohttp
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.main import redis


async def get_currencies(url: str) -> dict | bool:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return xmltodict.parse(await response.text())
            return False


async def update_currencies() -> None:
    data = await get_currencies('https://cbr.ru/scripts/XML_daily.asp')
    if not data:
        print('Ошибка при парсинге курса валют')
        return
    currencies = data['ValCurs']['Valute']
    for currency in currencies:
        currency_code = currency['CharCode']
        currency_value = currency['VunitRate'].replace(',', '.')
        await redis.set(name=currency_code, value=currency_value)


async def format_currencies() -> str:
    data = await get_currencies('https://cbr.ru/scripts/XML_daily.asp')
    if not data:
        print('Ошибка при парсинге курса валют')
        return
    currencies = data['ValCurs']['Valute']
    text = 'Актуальный курс валют:\n'
    for currency in currencies:
        text += f'{currency["Name"]} - {currency["VunitRate"]} рублей\n'
    return text


async def calculate_currencies(base: str, quote: str, amount: int) -> str:
    base_rate = float(await redis.get(name=base))
    quote_rate = float(await redis.get(name=quote))
    result = amount * base_rate / quote_rate
    return f'{result} рублей'


async def create_schedule() -> None:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_currencies, "interval", hours=24, start_date='2023-01-01 19:22:40', name='currencies')
    scheduler.start()
