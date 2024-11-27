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
import buttons


# All handlers should be attached to the Router (or Dispatcher)

TOKEN = ""

allids = {
    "startphoto" : "AgACAgIAAxkBAAMDZys6_3ZcFnD2Gh-OA7mP-e1KatQAAmPeMRvSMFhJbYBcP3pZ6BYBAAMCAAN4AAM2BA",
    "secpho" : "AgACAgIAAxkBAAMLZytRMv2FfSLfwvoJHsksEwdHA9UAAqzfMRvSMFhJdiYGvaoSDDYBAAMCAAN5AAM2BA",
    "logo" : "AgACAgIAAxkBAAMfZyusnQqQYM51DoUcjNCppq2bQzsAAi_jMRvSMFhJiUh7Y981Ci0BAAMCAAN5AAM2BA",
    "vid" : "BAACAgIAAxkBAAMuZyuwO509QNFkQAuGBbq0rP1znjIAAqZlAALSMFhJaEqLGv5_9ek2BA",
    "kakprim" : "AgACAgIAAxkBAAM6ZyuyV9l3BxxNbEFtg2aa1XJBlUkAAnfjMRvSMFhJ7yKRCn6oJ5IBAAMCAAN4AAM2BA",
    "screenshot" : "AgACAgIAAxkBAANqZyvQF3h-KDDMaRqxWTkDDIiCMqUAAsThMRs5E2BJ-i1x6_mctpcBAAMCAAN3AAM2BA",
    "howthatworks" : "AgACAgIAAxkBAAIBzWcuZlDWH45lm8TW6vD_vPnQisKDAAKQ5TEb2hZ5ScQGQ6k_0B-_AQADAgADeQADNgQ",
    "trackingofprod" : "AgACAgIAAxkBAAICAWcub8TQGLMI40mCdeTL11l_wjSgAALa5TEb2hZ5SaBfScxUwrMiAQADAgADeQADNgQ"
}


bot = Bot(TOKEN)
dp = Dispatcher()
router = Router()

# самая начальная команда старт 
@dp.message(Command("start"))
async def getstarted(message: Message):
    await message.answer_photo(allids["logo"],"""<b>Добро пожаловать в Primex:</b>
Ваш надежный партнер для экспресс доставки из Китая в Россию!

Мы доставляем посылки из любых китайских маркетплейсов во все регионы России, учитывая все потребности баеров и обеспечивая удобство и надежность на каждом этапе доставки.

""",parse_mode="HTML",reply_markup=buttons.mainkb)
    


# ответ на нажатие кнопки , 👉 Как пользоваться Primex 👈
@dp.callback_query(lambda callback_query: callback_query.data == "howtouse")
async def howtouse(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["kakprim"],"""В этом меню собраны все инструкции по использованию сервиса <b>Primex</b> 

Выберите интересующий вас пункт
""",parse_mode="HTML",reply_markup=buttons.sec)
    
    


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


""",parse_mode="HTML",reply_markup=buttons.howtotrack)
    
# ответ на нажатие кнопки Рассчитать доставку
@dp.callback_query(lambda callback_query: callback_query.data == "pricecount")
async def pricecount(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""<b>Стоимость за кг 6$
Срок доставки 12-15 дней

Вес округляется от1 кг.
Отправка товаров происходит 5 раза 
в неделю.</b>
""",parse_mode="HTML",reply_markup=buttons.backtomainmenu)




# видео склада в Китае 
@dp.callback_query(lambda callback_query: callback_query.data == "trackorder")
async def trackorder(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_video(allids["vid"],caption="""Наш склад оборудован всеми необходимыми материалами для безопасного хранения и обработки ваших посылок.

Мы работаем без выходных, чтобы принимать посылки <b>каждый день.</b>

Команда профессионалов тщательно проверяет каждую посылку и обеспечивает надежную упаковку для безопасной доставки""",parse_mode="HTML",reply_markup=buttons.backtomainmenu)



# лич кабинет
@dp.callback_query(lambda callback_query: callback_query.data == "kabin")
async def kabinlich(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["screenshot"],"""После регистрации вам станет доступен удобный <b>личный кабинет</b>, где вы найдете адреса наших складов с инструкциями по правильному заполнению данных. 
В личном кабинете вы сможете отслеживать свои посылки, заказывать выкуп товаров и подключать дополнительные услуги.
""",parse_mode="HTML",reply_markup=buttons.screen)
    
    
# как я буду отслеживать посылки 
@dp.callback_query(lambda callback_query: callback_query.data == "howwillitrack")
async def howwillitrack(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""<b>Чтобы отслеживать посылки, мы отправим вам на электронную почту три уведомления с подробной информацией</b>

Когда посылка поступит на наш склад

Когда мы отправим её к вам

Когда посылка прибудет в Москву


Вы также можете в любой момент отслеживать статус на нашем сайте: https://primexcargo.org/tracking


""",parse_mode="HTML")

# Помощь с выкупом 
@dp.callback_query(lambda callback_query: callback_query.data == "helpwithbuying")
async def helpwithbuying(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""<b>Если вам нужна помощь с выкупом, служба Primex сделает всё легко и просто!</b>

Купим товары с китайских маркетплейсов за вас в тот же день — быстро, удобно и доступно. 

Просто отправьте ссылку на нужный товар менеджеру - @PrimexCargo, и байер свяжется с вами в течение 2 часов в рабочее время.


""",parse_mode="HTML",reply_markup=buttons.justback)

# кнопка назад , которая возвращает где кнопка старт и сам логотип и основные кнопки
@dp.callback_query(lambda callback_query: callback_query.data == "back")
async def getback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["logo"],"""<b>Добро пожаловать в Primex: </b>
Ваш надежный партнер для экспресс доставки из Китая в Россию!

Мы доставляем посылки из любых китайских маркетплейсов во все регионы России, учитывая все потребности баеров и обеспечивая удобство и надежность на каждом этапе доставки.

""",parse_mode="HTML",reply_markup=buttons.mainkb)
    
# кнопка назад , чтобы увидеть 3 кнопки , как это рабоает , ссылка на регистрацию , помощь с выкупом
@dp.callback_query(lambda callback_query: callback_query.data == "backtohow")
async def getbacktohow(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["kakprim"],"""В этом меню собраны все инструкции по использованию сервиса <b>Primex</b> 

Выберите интересующий вас пункт
""",parse_mode="HTML",reply_markup=buttons.sec)
    
    
# возвращение с регистрации , туда где 3 кнопки 
@dp.callback_query(lambda callback_query: callback_query.data == "backfromregistration")
async def backfromregistration(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["kakprim"],"""В этом меню собраны все инструкции по использованию сервиса <b>Primex</b> 

Выберите интересующий вас пункт
""",parse_mode="HTML",reply_markup=buttons.sec)
    

# возвращение назад , с Купим товары с китайских маркетплейсов
@dp.callback_query(lambda callback_query: callback_query.data == "justback")
async def justback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["kakprim"],"""В этом меню собраны все инструкции по использованию сервиса <b>Primex</b> 

Выберите интересующий вас пункт

""",parse_mode="HTML",reply_markup=buttons.sec)


# возвращение в главное меню , с любого места 
@dp.callback_query(lambda callback_query: callback_query.data == "mainmenu")
async def getbacktomainmenu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["logo"],"""<b>Добро пожаловать в Primex: </b>
Ваш надежный партнер для экспресс доставки из Китая в Россию!

Мы доставляем посылки из любых китайских маркетплейсов во все регионы России, учитывая все потребности баеров и обеспечивая удобство и надежность на каждом этапе доставки.

""",parse_mode="HTML",reply_markup=buttons.mainkb)


# Ответы на популярные вопросы 
@dp.callback_query(lambda callback_query: callback_query.data == "qa")
async def questionanswer(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""<b>В данном меню собраны ответы на самые популярные вопросы</b>
""",parse_mode="HTML",reply_markup=buttons.answerstoquestions)
    
# deliverytime
@dp.callback_query(lambda callback_query: callback_query.data == "deliverytime")
async def deliverytime(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""Срок доставки до Москвы составляет 12-15 дней дней с момента отправки
""",parse_mode="HTML")

@dp.callback_query(lambda callback_query: callback_query.data == "howtotrackorders")
async def howtotrackorders(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(allids["trackingofprod"],"""<b>Чтобы отслеживать посылки, мы отправим вам на электронную почту три уведомления с подробной информацией</b>

Когда посылка поступит на наш склад

Когда мы отправим её к вам

Когда посылка прибудет в Москву


Вы также можете в любой момент отслеживать статус на нашем сайте: https://primexcargo.org/tracking

""",parse_mode="HTML")
    
@dp.callback_query(lambda callback_query: callback_query.data == "rulesofgetting")
async def rulesofgetting(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("""После прибытия груза вам на электронную почту будет отправлено письмо с расчетом
и ссылкой на менеджера. Необходимо оплатить, отправить чек и оформить доставку
по России в личном кабинете.
""",parse_mode="HTML")









 


async def main() -> None:
    
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


