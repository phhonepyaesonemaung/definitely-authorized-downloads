import os
import sys
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateForumTopicRequest

api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
bot_token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = int(os.environ['TELEGRAM_CHAT_ID'])

folder_path = sys.argv[1]
course_name = sys.argv[2]

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def main():
    print(f"Creating topic: {course_name}")
    
    # Telegram limits topic names to 128 characters, so we slice the string just in case
    topic = await client(CreateForumTopicRequest(
        channel=chat_id,
        title=course_name[:128]
    ))
    
    # Safely extract the new Topic ID from the Telegram API response
    topic_id = None
    for update in topic.updates:
        if hasattr(update, 'message') and hasattr(update.message, 'id'):
            topic_id = update.message.id
            break
        elif hasattr(update, 'id'):
            topic_id = update.id
            break

    await client.send_message(chat_id, f"📚 **{course_name}**\n\nUploading materials...", reply_to=topic_id)
    
    for root, dirs, files in os.walk(folder_path):
        for file in sorted(files): 
            if file.startswith('.'): continue
            file_path = os.path.join(root, file)
            print(f"Uploading {file}...")
            try:
                await client.send_file(chat_id, file_path, caption=f"🎬 {file}", reply_to=topic_id)
            except Exception as e:
                print(f"Failed to upload {file}: {e}")

with client:
    client.loop.run_until_complete(main())
