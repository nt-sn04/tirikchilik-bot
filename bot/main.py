from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)

from .config import settings
from .handlers import (
    start_command,
    cart_hendler,
    select_lang_hendler,
    change_lang_query,
)


def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    # comand handlers
    dispatcher.add_handler(CommandHandler(command="start", callback=start_command))

    # messge handlers
    dispatcher.add_handler(MessageHandler(
        filters=Filters.text('📥 Savatcha'),
        callback=cart_hendler
    ))
    dispatcher.add_handler(MessageHandler(
        filters=Filters.text('Tilni tanlash'),
        callback=select_lang_hendler
    ))

    # callback query handlers
    dispatcher.add_handler(CallbackQueryHandler(
        callback=change_lang_query,
        pattern='lang:'
    ))

    updater.start_polling()
    updater.idle()
