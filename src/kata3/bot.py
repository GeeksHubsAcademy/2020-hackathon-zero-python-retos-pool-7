import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    return update.message.reply_text('Hola, Geeks!')


def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    return update.message.reply_text('Ayudame!')


def mayus(update, context):
    textUpper = " ".join(map(lambda x:x.upper(), context.args))
    return update.message.reply_text(textUpper)


def alreves(update, context):
    """Repite el mensaje del usuario."""
    textReverse = update.message.text[::-1]
    message = update.message.reply_text(textReverse)

    return message


def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Inicio del Bot"""
    # Colocamos el Token creado por FatherBot
    updater = Updater(
        "1128656921:AAFAGXhcCwDeySb8nz8Jx37Ng3a2jN6eG88", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mayus", mayus))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    dp.add_handler(MessageHandler(Filters.text, alreves))

    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
