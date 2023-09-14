import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot Telegram
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Créez un dictionnaire pour stocker l'état de l'utilisateur
user_data = {}

# Fonction de gestion de la commande /start
def start(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=f"Bienvenue sur Solkah VIP, {user.first_name}!")
    
    # Création des boutons inline
    keyboard = [
        [InlineKeyboardButton("S'inscrire au VIP", callback_data='inscription')],
        [InlineKeyboardButton("Comment payer", callback_data='paiement')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Que souhaitez-vous faire ?", reply_markup=reply_markup)

# Fonction de gestion des boutons inline
def button(update, context):
    query = update.callback_query
    user_id = query.message.chat_id

    if query.data == 'inscription':
        context.bot.send_message(chat_id=user_id, text="Veuillez effectuer le dépôt sur l'adresse Tron : udirufjrururjrjrjrurjr")
    elif query.data == 'paiement':
        context.bot.send_message(chat_id=user_id, text="Regardez la vidéo pour savoir comment effectuer le paiement.")

# Fonction principale
def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Gestion de la commande /start
    dp.add_handler(CommandHandler("start", start))

    # Gestion des boutons inline
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
