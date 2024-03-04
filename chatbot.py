from typing import Final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


TOKEN: Final = '6495214817:AAEjqvvQ5CY2l36UtgZ26PFxCYzhS0V2qa8'

BOT_USERNAME: Final = '@YumYumCoffeeBot'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your Coffee Bot. Send me a what you have, and I will tell you what coffee you can make.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()