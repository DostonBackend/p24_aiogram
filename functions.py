from pprint import pprint

from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputFile, user

from states import SignUp


async def info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    data = f""" Sizning ismingiz : {user.first_name} \nId raqamingiz: {user.id} \n"""
    if user.username:
        data += f"Siznig usernameiz @{user.username}\n"
    if user.last_name:
        data += f"Sizning familyangiz {user.last_name}\n"
    if profile.bio:
        data += f"Sizning bioingiz {profile.bio}\n"
    pprint(data)
    await message.answer(text=data)


# -------------------------start_menu-------------------------
async def start_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Assalomu alaykum {message.from_user.first_name} "
                         "\nUstoz Shogird kanalining Botiga xush kelibsiz!"
                         "\n\n/help yordam buyrug`i orqali bot nimalar qila olishini bilib oling! ")
    pprint(message.text)


# ---------------------------help----------------------------
async def help(message: Message, bot: Bot, state: FSMContext):
    await message.answer("""
/start -> Botni ishga tushirish
/help -> Commandlarni ko`rish
/info -> Telegram Ma`lumotlarizngiz
/vacancy -> E`lon berish
    """
                         )
    pprint(message.text)


# ------------------------Vacancy----------------------
async def vacancy(message: Message, bot: Bot, state: FSMContext):
    await message.answer(
        "🎓 Idora nomi?: "
    )
    await state.set_state(SignUp.idora_nomi)


async def register_idora_nomi(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(idora_nomi=message.text)
    await message.answer(
        "📚 Texnologiya:\n\n"
        "Talab qilinadigan texnalogiyalarni kiriting?\n"
        "Texnologiya nomlarini vergul bilan ajrating. Masalan,\n\n"
        "Python, django, Api"
    )
    await state.set_state(SignUp.texnalogiya)


async def register_texnalogiya(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(texnalogiya=message.text)
    await message.answer(
        "📞 Aloqa: \n\n"
        "Bog`lanish uchun raqamingizni kiriting?\n"
        "Masalan, +998 90 123 45 67"
    )
    await state.set_state(SignUp.phone)


async def register_phone(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer(
        "🌐 Hudud: \n\n"
        "Qaysi Hududdansiz?\n"
        "Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."
    )
    await state.set_state(SignUp.hudud)


async def register_hudud(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer(
        "✍️Mas'ul ism sharifi?"

    )
    await state.set_state(SignUp.masul_shaxs_user_name)


async def register_masul_shaxs_user_name(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(masul_shaxs_user_name=message.text)
    await message.answer(
        "🕰 Murojaat qilish vaqti: \n\n"
        "Qaysi vaqtda murojaat qilish mumkin?"
        "Masalan, 9:00 - 18:00"
    )
    await state.set_state(SignUp.murojat_vaqti)


async def register_murojat_vaqti(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(murojat_vaqti=message.text)
    await message.answer(
        "🕰 Ish vaqtini kiriting? "

    )
    await state.set_state(SignUp.ish_vaqti)


async def register_ish_vaqti(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(ish_vaqti=message.text)
    await message.answer(
        "💰 Maoshni kiriting?"

    )
    await state.set_state(SignUp.maosh)


async def finish(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(maosh=message.text)
    user = message.from_user
    data = await state.get_data()
    txt = f'''E`loningiz Tayyor!\n
🏢 Idora: {data.get("idora_nomi")}
<b>📚 Texnologiya: {data.get("texnalogiya")} </b>
🇺🇿 Telegram: @{data.get("masul_shaxs_user_name")} 
📞 Aloqa: {data.get("phone")}
🌐 Hudud: {data.get("hudud")}
✍️ Mas'ul: {data.get("masul_shaxs_user_name")}
🕰 Murojaat vaqti: {data.get("murojat_vaqti")}
🕰 Ish vaqti: {data.get("ish_vaqti")}
<b><u>💰 Maosh: {data.get("maosh")} </u></b>\n
#ishjoyi #{data.get("texnologiya")} #{data.get("hudud")}

    '''
    await message.answer("Qabul qilindi ✅ Kanalimizni kuzatib boring😉")
    await message.answer(txt, parse_mode="html")
    await bot.send_message(chat_id="1313375286", text=txt, parse_mode='html')
    # return pprint(bot.send_message(chat_id="1313375286", text=txt))


async def start(bot: Bot):
    await bot.send_message(chat_id="1313375286", text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="1313375286", text="Bot To'xtadi ⚠️")
