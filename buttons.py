from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton , KeyboardButton , ReplyKeyboardRemove


# стартовская кнопка  
mainkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👉 Как пользоваться Primex 👈",callback_data="howtouse")
            
        ],
        [
            InlineKeyboardButton(text="Отзывы ⭐",url="https://t.me/Primexchina_otzyvy"),
            InlineKeyboardButton(text="Отчет 📖 ",url="https://t.me/ReportPRChina")
            
        ],
        [
            InlineKeyboardButton(text="Склад в Китае 🇨🇳",callback_data="trackorder")
            
        ],
        [
            InlineKeyboardButton(text="Поставщики 🚛",url="https://t.me/+TmwR3aRqCsM5NmQy")
            
        ],
        [
            InlineKeyboardButton(text="Рассчитать доставку 📲",callback_data="pricecount")
            
        ],
        [
            InlineKeyboardButton(text="Ответы на вопросы 💬",callback_data="qa")
            
        ],
        [
            InlineKeyboardButton(text="Связатся с мэнеджером 👤",url="https://t.me/PrimexCargo")
            
        ],
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
            InlineKeyboardButton(text="Помощь с выкупом",callback_data="helpwithbuying")
            
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="back")
            
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
            InlineKeyboardButton(text="Назад ↩",callback_data="backfromregistration")
            
        ]
        
    ],
    resize_keyboard=True
)


howtotrack = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Как я буду отслеживать посылки?",callback_data="howwillitrack")
            
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="backtohow")
            
        ] 
    ],
    resize_keyboard=True
)


justback = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="justback")
            
        ] 
    ],
    resize_keyboard=True
)

backtomainmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="mainmenu")
            
        ] 
    ],
    resize_keyboard=True
)

answerstoquestions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Какие сроки доставки?",callback_data="deliverytime")
            
        ],
        [
            InlineKeyboardButton(text="Как отслеживать посылки?",callback_data="howtotrackorders")
            
        ],
        [
            InlineKeyboardButton(text="Правила получения посылки",callback_data="rulesofgetting")
            
        ],
        [
            InlineKeyboardButton(text="Назад ↩",callback_data="mainmenu")
            
        ]
    ],
    resize_keyboard=True
)






























