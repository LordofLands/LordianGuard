import os
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application

# TOKEN = '6857806736:AAGD0SyGIQaBHbGDjjTzRAG0XXlzg7qYcb0'
TOKEN = os.getenv('BOTAPIKEY')
BOT_USERNAME = '@LordianGuard_bot'


async def presaleCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(update.message.chat_id, 'Presale is on Dec 22nd 00:00 UTC')

async def launchCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(update.message.chat_id, 'Launch is on Dec 23rd 00:00 UTC')

async def marketingCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please contact @BrianR_8 or @GodofJoy1 for marketing')


def main():
    app = Application.builder().token(TOKEN).build()
    print("Starting bot...")

    app.add_handler(CommandHandler('presale', presaleCommand))
    app.add_handler(CommandHandler('launch', launchCommand))
    app.add_handler(CommandHandler('marketing', marketingCommand))

    print("Polling...")
    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'YOUR-CODECAPSULES-URL-HERE' + '/' + TOKEN
    app.start_webhook(listen='0.0.0.0', port=PORT, url_path=TOKEN, webhook_url=HOOK_URL)
    app.idle()

if __name__ == '__main__':
    main()
