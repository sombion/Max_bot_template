from maxapi.types import CallbackButton


from maxapi.utils.inline_keyboard import InlineKeyboardBuilder


async def create_start_btn():
    builder = InlineKeyboardBuilder()

    builder.row(CallbackButton(text="Кнопка 1", payload="btn_1"))
    builder.row(CallbackButton(text="Кнопка 2", payload="btn_2"))

    return builder.as_markup()
