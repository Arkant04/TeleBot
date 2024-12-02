import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Define el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Enviar el mensaje "Hola Mundo" y un número aleatorio
    random_number = random.randint(1, 100)  # Número aleatorio entre 1 y 100
    await update.message.reply_text(f"Hola Mundo! Aquí tienes un número aleatorio: {random_number}")

def main():
    # Reemplaza 'YOUR_API_KEY' con tu API key
    application = Application.builder().token("mi api").build()

    # Registra el comando /start
    application.add_handler(CommandHandler("start", start))

    # Comienza a escuchar los mensajes
    application.run_polling()

if __name__ == '__main__':
    main()
