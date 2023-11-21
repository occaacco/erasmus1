from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("https://github.com/occaacco/erasmus1")


app = ApplicationBuilder().token("6918073482:AAHKlosyyeQcU8_J-g2H3yLhJsR6l-TvemM").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()