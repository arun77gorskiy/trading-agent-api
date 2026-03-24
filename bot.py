import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "ТВОЙ_ТОКЕН_СЮДА"

API_URL = "https://your-app.onrender.com/signal"

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = requests.get(API_URL)
    data = res.json()

    await update.message.reply_text(str(data))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("signal", signal))

app.run_polling()
