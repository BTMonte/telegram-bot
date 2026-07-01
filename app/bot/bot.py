from telegram.ext import Application, CommandHandler
from app.bot.handlers import start_command


def create_application(token: str) -> Application:
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))

    return app
