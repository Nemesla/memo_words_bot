from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Start')


@router.message(Command('help'))
async def help(message: Message):
    await message.answer("Help")

@router.message(F.text == "Hello")
async def hello(message: Message):
    await message.answer("Hello")
    
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")