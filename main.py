from telegram import *
from telegram.ext import *
from requests import *

import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


updater = Updater(token="5522269859:AAHYiP4qDKtVndALtubKKDa1tAg1XZ272Pc")

MemeText = "Memlar"
ImageText = "Rasmlar"

MemeUrl = "https://api.memegen.link/images/buzz/memes/memes_everywhere.gif"
ImageUrl = "https://picsum.photos/200"

likes = 0
dislikes = 0

allowedUsernames = ['vonikreus']


def start(update: Update, context: CallbackContext):
    user = update.effective_user['first_name']
    buttons = [[KeyboardButton(ImageText)], [
        KeyboardButton(MemeText)]]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Assalom alleykum, xush kelibsiz {user}!", reply_markup=ReplyKeyboardMarkup(buttons))


def message(update: Update, context: CallbackContext):
    if update.effective_chat.username not in allowedUsernames:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Siz botdan foydalanish huquqiga ega emassiz!")
        return
    if MemeText in update.message.text:
        meme = get(MemeUrl).content
        if meme:
            context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                InputMediaPhoto(meme, caption="")])

        buttons = [[InlineKeyboardButton("👍", callback_data="yoqdi")], [
            InlineKeyboardButton("👎", callback_data="yoqmadi")], [InlineKeyboardButton("◀️", callback_data="Orqaga")], [InlineKeyboardButton("➡️", callback_data="Keyingisi")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
            buttons), text="Meme kulgulimi 😁?")

    if ImageText in update.message.text:
        image = get(ImageUrl).content
        if image:
            context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                InputMediaPhoto(image, caption="")])

        buttons = [[InlineKeyboardButton("👍", callback_data="yoqdi")], [
            InlineKeyboardButton("👎", callback_data="yoqmadi")], [InlineKeyboardButton("◀️", callback_data="Orqaga")], [InlineKeyboardButton("➡️", callback_data="Keyingisi")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
            buttons), text="Rasm yoqdimi?")





def query(update: Update, context: CallbackContext)->None:
    query = update.callback_query.data
    update.callback_query.answer()

    global likes, dislikes

    if "yoqdi" in query:
        likes += 1

    if "yoqmadi" in query:
        dislikes += 1

<<<<<<< HEAD
    print(f"yoqqanlari -> {likes} va yoqmagalari -> {dislikes}")
=======
    print(f"yoqqanlari = {likes} \n yoqmagalari = {dislikes}")
>>>>>>> 6f3b9fc894799c048ac88cd41dcec67e305ce94f


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text, message))
dispatcher.add_handler(CallbackQueryHandler(query))

updater.start_polling()
