from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from src.funcs import calculate_currencies, format_currencies

main_router = Router()


@main_router.message(Command('gid'))
async def gid(message: Message) -> None:
    await message.answer(text=str(message.chat.id))


@main_router.message(Command('id'))
async def ids(message: Message) -> None:
    await message.answer(text=str(message.from_user.id))


@main_router.message(Command('start'))
async def start(message: Message) -> None:
    name = message.from_user.username if message.from_user.username else message.from_user.first_name
    await message.answer(text=f'Привет, {name}\n'
                              f'Доступные команды:\n'
                              f'/exchange [CURRENCY FROM] [CURRENCY TO] [AMOUNT]\n'
                              f'/rates')


@main_router.message(Command('rates'))
async def rates(message: Message) -> None:
    text = await format_currencies()
    await message.answer(text=text)


@main_router.message(Command('exchange'))
async def exchange(message: Message, command: CommandObject) -> None:
    print(type(command.args))
    base, quote, amount = command.args.split()
    result = await calculate_currencies(base, quote, int(amount))
    await message.answer(text=result)
