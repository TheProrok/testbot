from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Токен вашего бота
TOKEN = '7367197292:AAFpcWAxgv9IP-taLXWttjlEv7govkRO2aM'

# Функция, которая вызывается при старте
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я твой личный помощник.')
    # await show_menu(update)

# Функция для отображения основного меню
async def show_menu(update: Update) -> None:
    # Создаем клавиатуру ReplyKeyboardMarkup
    reply_keyboard = [
        ["Дельта С", "Коэф. запаса"],
        ["Расчет ТАУ"]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    await update.message.reply_text(
        'Чем ещё могу помочь?',
        reply_markup=reply_markup
    )

# Функция, которая вызывается при нажатии кнопок ReplyKeyboardMarkup
async def handle_reply_keyboard(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text

    if user_text == "Дельта С":
        await update.message.reply_text('Дельта С расчитывается так: C2-C1*100/C1')
    elif user_text == "Коэф. запаса":
        await update.message.reply_text('Коэффициент запаса рассчитывается так: Норму разделить на максимальное значение')
    elif user_text == "Расчет ТАУ":
        await update.message.reply_text('ТАУ расчитывается так: Rиз в/в (без степеней) * на ёмкость')

    # Повторно отправляем клавиатуру
    await show_menu(update)

def main() -> None:
    # Создаем объект Application и передаем ему токен
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик нажатий на кнопки ReplyKeyboardMarkup
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply_keyboard))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    print('Бот тест работает')
    main()
