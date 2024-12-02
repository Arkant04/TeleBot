import random
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Define el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Obtener el primer nombre del usuario
    user_first_name = update.message.from_user.first_name

    # Generar un número aleatorio
    random_number = random.randint(1, 100)  # Número aleatorio entre 1 y 100

    # Saludo personalizado
    await update.message.reply_text(f"¡Hola {user_first_name}! Aquí tienes un número aleatorio: {random_number}")

# Define el comando /saludo para recibir un nombre y saludarlo
async def saludo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Verificar si el usuario proporcionó un nombre (si no, se usa el nombre por defecto)
    if context.args:
        nombre_personalizado = " ".join(context.args)  # Juntar los argumentos que el usuario envió
        await update.message.reply_text(f"¡Hola, {nombre_personalizado}! ¡Qué gusto saludarte!")
    else:
        # Si el usuario no proporcionó un nombre, se manda un mensaje por defecto
        await update.message.reply_text("Por favor, ingresa un nombre para saludar. Ejemplo: /saludo Juan")

# Define el comando /ping para hacer un ping a Google
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Ejecuta el comando ping a Google
        result = subprocess.run(['ping', 'google.com', '-c', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Si la ejecución es exitosa, enviar los resultados del ping
        if result.returncode == 0:
            # Enviar los resultados del ping al usuario
            await update.message.reply_text(f"Ping a Google exitoso:\n{result.stdout}")
        else:
            await update.message.reply_text("Hubo un error al intentar hacer el ping a Google.")
    except Exception as e:
        await update.message.reply_text(f"Hubo un error al ejecutar el comando: {e}")

def main():
    # Reemplaza 'YOUR_API_KEY' con tu API key
    application = Application.builder().token("mi api").build()

    # Registra el comando /start
    application.add_handler(CommandHandler("start", start))

    # Registra el comando /saludo
    application.add_handler(CommandHandler("saludo", saludo))

    # Registra el comando /ping
    application.add_handler(CommandHandler("ping", ping))

    # Comienza a escuchar los mensajes
    application.run_polling()

if __name__ == '__main__':
    main()
