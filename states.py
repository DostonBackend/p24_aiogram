from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    idora_nomi = State()
    texnalogiya = State()
    phone = State()
    hudud = State()
    masul_shaxs_user_name = State()
    murojat_vaqti = State()
    ish_vaqti = State()
    maosh = State()
    qoshimcha = State()
