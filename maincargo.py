import json
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types , F 
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart , Command
from aiogram.types import Message , CallbackQuery ,FSInputFile
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton 
from aiogram.methods import SendMediaGroup
from aiogram.types import InputMediaPhoto 
from aiogram.types import ContentType
import buttonscargo


# All handlers should be attached to the Router (or Dispatcher)

TOKEN = "?" # Primex Cargo

allids = {
    "logo" : "AgACAgIAAxkBAAMCZy5MSDbnOviB_VCBeJ1NfhO5e08AAuvpMRtu9XBJdEY8CocI19EBAAMCAAN5AAM2BA",# логотип
    "screenshot" : "AgACAgIAAxkBAANBZy5XJM0LO6t-8WLd_P7UzjuVcYIAAhbqMRtu9XBJYweP8PLNla8BAAMCAAN5AAM2BA", # скрин личного кабинета
    "howthatworks" : "AgACAgIAAxkBAAN4Zy5lJG6m7B1vOwuRnghLe4VU89EAApDlMRvaFnlJOBT3H9GP52wBAAMCAAN5AAM2BA", # склад в голом виде
    "howtotrackorder" : "AgACAgIAAxkBAAOOZy5xmwPJ_jq0vNluNrGixnNTOYMAAtrlMRvaFnlJCwYlH5efNBQBAAMCAAN5AAM2BA",# мужик ищет заказ
    "cutewoman" : "AgACAgIAAxkBAAPIZy54PKnxb-onUDzwriX2LQI0yfMAApTrMRtu9XBJEGTDpRqPi7sBAAMCAAN4AAM2BA" # милая женщина 
}


bot = Bot(TOKEN)
dp = Dispatcher()
router = Router()

# самая начальная команда старт 
@dp.message(Command("start"))
async def getstarted(message: Message):
    await message.answer_photo(allids["logo"],"""<b>Добро пожаловать в Primex:</b>
Мы являемся сервисом по доставке ваших любимых брендов из любого американского, китайского, турецкого и европейского сайта и маркетплейса во все регионы России.

""",parse_mode="HTML",reply_markup=buttonscargo.mainkb)
    






# ответ на нажатие кнопки , 👉 Как пользоваться Primex 👈
@dp.callback_query(lambda callback_query: callback_query.data == "howtouse")
async def howtouse(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["cutewoman"],"""В этом меню собраны все инструкции по использованию сервиса <b>Primex</b> 

Выберите интересующий вас пункт
""",parse_mode="HTML",reply_markup=buttonscargo.sec)
    
    
# ответ на нажатие кнопки , Как это работает ? 
@dp.callback_query(lambda callback_query: callback_query.data == "howthisworks")
async def howthisworks(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["howthatworks"],"""<b>Регистрация</b>

Чтобы начать работу с нами, необходимо
пройти
быструю регистрацию для того чтобы получить адрес склада в Китае


<b>Выкуп товара</b>

Заказывайте товары из Китайских
маркетплейсов к нам на склад в Гуанчжоу


<b>Прием и отправка</b>

После получения на складе ваших заказов
Мы их консолидируем, упакуем и готовим к отправке


<b>Доставляем до ваших рук</b>

Доставляем во все регионы России. До Вашего
адреса или до ближайшего пункта выдачи.


""",parse_mode="HTML",reply_markup=buttonscargo.howtotrack)

# вовзращение к как это работает и ссылка на рег
@dp.callback_query(lambda callback_query: callback_query.data == "backtohowtouse")
async def backtohowtouse(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["cutewoman"],"""В этом меню собраны все инструкции по использованию сервиса <b>Primex</b> 

Выберите интересующий вас пункт
""",parse_mode="HTML",reply_markup=buttonscargo.sec)


# регистрация и скриншот 
@dp.callback_query(lambda callback_query: callback_query.data == "kabin")
async def kabin(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["screenshot"],"""После регистрации вам станет доступен удобный личный кабинет, где вы найдете адреса наших складов с инструкциями по правильному заполнению данных. 
В личном кабинете вы сможете отслеживать свои посылки, заказывать выкуп товаров и подключать дополнительные услуги.
""",reply_markup=buttonscargo.screen)


# backtomainkb возвращение к главной менюшке 
@dp.callback_query(lambda callback_query: callback_query.data == "backtomainkb")
async def backtomainkb(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["logo"],"""Мы являемся сервисом по доставке ваших любимых брендов
из любого американского, китайского, турецкого и европейского сайта и маркетплейса во все регионы России.

""",parse_mode="HTML",reply_markup=buttonscargo.mainkb)
    
    

# кнопка назал usachi
@dp.callback_query(lambda callback_query: callback_query.data == "usachi")
async def usachi(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Здесь стоимость для каждой страны.
""",reply_markup=buttonscargo.pricecount)
    
# Рассчитать стоимость 
@dp.callback_query(lambda callback_query: callback_query.data == "pricecount")
async def pricecount(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Здесь стоимость для каждой страны.
""",reply_markup=buttonscargo.pricecount)
    
    
# США
@dp.callback_query(lambda callback_query: callback_query.data == "us")
async def us(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Стоимость за кг 17$.
Срок доставки 14-16 дней.
Вес округляется от 1 кг.
Отправка происходит 1 раз в неделю.


""",reply_markup=buttonscargo.backtocountries)
    
    
#Китай
@dp.callback_query(lambda callback_query: callback_query.data == "cn")
async def cn(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Стоимость за кг 7$.
Срок доставки 12-15 дней.
Вес округляется от 1 кг.
Отправка товаров происходит 5 раз в неделю.

""",reply_markup=buttonscargo.backtocountries)
    
    
# Турция 
@dp.callback_query(lambda callback_query: callback_query.data == "tu")
async def tu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Стоимость за кг 10$.
Срок доставки 4-5 дней.
Вес округляется от 1 кг.
Отправка товаров происходит 5 раз в неделю.


""",reply_markup=buttonscargo.backtocountries)
    
    
# Италия
@dp.callback_query(lambda callback_query: callback_query.data == "it")
async def it(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Стоимость за кг 17€.
Срок доставки 14-16 дней.
Вес округляется от 1 кг.
Отправка товаров происходит 1 раз в неделю.

""",reply_markup=buttonscargo.backtocountries)

# помощь с выкупом helpwithbuying
@dp.callback_query(lambda callback_query: callback_query.data == "helpwithbuying")
async def helpwithbuying(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Ваш личный байер в мире международных покупок.

Служба <b>Primex</b> поможет легко приобрести товары в зарубежных интернет-магазинах. Выкупим товары с сайтов за вас в тот же день – быстро, легко и доступно.

После заполнения заявки, байер - @PrimexCargo, сам с вами свяжется в течение 2-х часов в рабочее время.


""",parse_mode="HTML",reply_markup=buttonscargo.backtomainmenu)


# ответы на вопросы 
@dp.callback_query(lambda callback_query: callback_query.data == "qa")
async def qa(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""В данном меню собраны ответы на самые популярные вопросы
""",reply_markup=buttonscargo.otvetynavop)


# Как отслеживать посылки ?
@dp.callback_query(lambda callback_query: callback_query.data == "howtotrackorders")
async def howtotrackorders(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["howtotrackorder"],"""<b>Чтобы отслеживать посылки, мы отправим вам на электронную почту три уведомления с подробной информацией</b>

Когда посылка поступит на наш склад

Когда мы отправим её к вам

Когда посылка прибудет в Москву


Вы также можете в любой момент отслеживать статус на нашем сайте: https://primexcargo.org/tracking
""",parse_mode="HTML",reply_markup=buttonscargo.backtoquest)

# Правила получения посылки
@dp.callback_query(lambda callback_query: callback_query.data == "rulesofgetting")
async def rulesofgetting(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""После прибытия груза вам на электронную почту будет отправлено письмо с расчетом
и ссылкой на менеджера. Необходимо оплатить, отправить чек и оформить доставку
по России в личном кабинете.
""",parse_mode="HTML",reply_markup=buttonscargo.backtoquest)


# назад к вопросам 
@dp.callback_query(lambda callback_query: callback_query.data == "backtoqa")
async def backtoqa(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""В данном меню собраны ответы на самые популярные вопросы
""",reply_markup=buttonscargo.otvetynavop)





 


async def main() -> None:
    
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


