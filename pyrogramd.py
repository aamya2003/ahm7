from pyrogram import Client, filters

bot_token = "5441497314:AAF5gj27qkohYLDfPxIBi6Jj_isAb7cnF3w"

api_id = 29551577
api_hash = "d09fb1a2667ade3fbd78a6586d6d945e"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()
