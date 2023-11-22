from github import Github # give access to github
import asyncio
from telegram import Bot # send data to the telegram bot

# send message to telegram chat
async def send_telegram_message(message):

    bot_token = "6918073482:AAHKlosyyeQcU8_J-g2H3yLhJsR6l-TvemM"
    chat_id = "-4005527088"

    # Create a bot instance
    bot = Bot(token=bot_token)

    # Send the text message
    await bot.send_message(chat_id=chat_id, text=message)

# repository path
rep = "occaacco/erasmus1"

# Github access
my_git = Github("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")
base_files = list(my_git.get_repo(rep).get_contents(""))

# Run the asyncio event loop

loop = asyncio.get_event_loop()

# Run the main loop
while True:
    if new_reps := [i for i in list(my_git.get_repo(rep).get_contents("")) if i not in base_files]:
        for i in new_reps:
            loop.run_until_complete(send_telegram_message("Someone uploaded a file to Github. \n" + str(i.html_url)))
            base_files.append(i)

# Close the event loop
loop.close()