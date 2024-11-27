<<<<<<< HEAD
from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton , KeyboardButton , ReplyKeyboardRemove


# стартовская кнопка  
mainkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👉 Как пользоваться Primex 👈",callback_data="howtouse")
            
        ],
        [
            InlineKeyboardButton(text="Отзывы ⭐",url="https://t.me/otzyvyprimex"),
            InlineKeyboardButton(text="Отчет 📖 ",url="https://t.me/Reportprime")
            
        ],
        [
            InlineKeyboardButton(text="Рассчитать стоимость 📲",callback_data="pricecount")
            
        ],
        [
            InlineKeyboardButton(text="Помощь с выкупом 💸",callback_data="helpwithbuying")
            
        ],
        [
            InlineKeyboardButton(text="Ответы на вопросы 💬",callback_data="qa")
            
        ],
        [
            InlineKeyboardButton(text="Наш общий чат 💭",url="https://t.me/primexecchat")
            
        ],
        [
            InlineKeyboardButton(text="Наш сайт 💻",url="https://primexcargo.org")
            
        ]
    ],
    resize_keyboard=True
)

sec = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Как это работает?",callback_data="howthisworks")
            
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Ссылка на регистрацию",callback_data="kabin")
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb")
            
        ]
    ],
    resize_keyboard=True
)

screen = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ссылка на регистрацию",url="https://primexcargo.org/registration")
            
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtohowtouse")
            
        ]
        
    ],
    resize_keyboard=True
)


howtotrack = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtohowtouse")
            
        ] 
    ],
    resize_keyboard=True
)


backtocountries = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="usachi")
            
        ] 
    ],
    resize_keyboard=True
)


backtomainmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Заказать выкуп 📩",url="https://primex1.vercel.app/services?service=purchase") # Обновление кнопки 
   
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb") # кнопка назад 
        ]
    ],
    resize_keyboard=True
)






pricecount = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="США 🇺🇸",callback_data="us")
            
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Китай 🇨🇳",callback_data="cn")
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Турция 🇹🇷",callback_data="tu")
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Италия 🇮🇹",callback_data="it")
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb")
            
        ]
    ],
    resize_keyboard=True
)




otvetynavop = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Как отслеживать посылки ?",callback_data="howtotrackorders")
            
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Правила получения посылки",callback_data="rulesofgetting")
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb")
            
        ]
    ],
    resize_keyboard=True
)


backtoquest = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtoqa")
            
        ]
    ],
    resize_keyboard=True
=======
from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton , KeyboardButton , ReplyKeyboardRemove


# стартовская кнопка  
mainkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👉 Как пользоваться Primex 👈",callback_data="howtouse")
            
        ],
        [
            InlineKeyboardButton(text="Отзывы ⭐",url="https://t.me/otzyvyprimex"),
            InlineKeyboardButton(text="Отчет 📖 ",url="https://t.me/Reportprime")
            
        ],
        [
            InlineKeyboardButton(text="Рассчитать стоимость 📲",callback_data="pricecount")
            
        ],
        [
            InlineKeyboardButton(text="Помощь с выкупом 💸",callback_data="helpwithbuying")
            
        ],
        [
            InlineKeyboardButton(text="Ответы на вопросы 💬",callback_data="qa")
            
        ],
        [
            InlineKeyboardButton(text="Наш общий чат 💭",url="https://t.me/primexecchat")
            
        ],
        [
            InlineKeyboardButton(text="Наш сайт 💻",url="https://primexcargo.org")
            
        ]
    ],
    resize_keyboard=True
)

sec = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Как это работает?",callback_data="howthisworks")
            
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Ссылка на регистрацию",callback_data="kabin")
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb")
            
        ]
    ],
    resize_keyboard=True
)

screen = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ссылка на регистрацию",url="https://primexcargo.org/registration")
            
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtohowtouse")
            
        ]
        
    ],
    resize_keyboard=True
)


howtotrack = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtohowtouse")
            
        ] 
    ],
    resize_keyboard=True
)


backtocountries = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="usachi")
            
        ] 
    ],
    resize_keyboard=True
)


backtomainmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb")
            
        ]
    ],
    resize_keyboard=True
)






pricecount = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="США 🇺🇸",callback_data="us")
            
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Китай 🇨🇳",callback_data="cn")
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Турция 🇹🇷",callback_data="tu")
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Италия 🇮🇹",callback_data="it")
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb")
            
        ]
    ],
    resize_keyboard=True
)




otvetynavop = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Как отслеживать посылки ?",callback_data="howtotrackorders")
            
        ],
        [ # https://primexcargo.org/registration
            InlineKeyboardButton(text="Правила получения посылки",callback_data="rulesofgetting")
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtomainkb")
            
        ]
    ],
    resize_keyboard=True
)


backtoquest = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtoqa")
            
        ]
    ],
    resize_keyboard=True
>>>>>>> 0d7c3deb826d3e81cc4e712ee8fe2fbc6dd6f3c1
)