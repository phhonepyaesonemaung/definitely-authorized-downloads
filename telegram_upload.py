import os
import sys
import json
import urllib.request
from telethon.sync import TelegramClient

api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
bot_token = os.environ['TELEGRAM_BOT_TOKEN']
chat_id = int(os.environ['TELEGRAM_CHAT_ID'])

folder_path = sys.argv[1]
course_name = sys.argv[2]

# 1. Create the topic using Telegram's standard HTTP Bot API
url = f"https://api.telegram.org/bot{bot_token}/createForumTopic"
payload = json.dumps({"chat_id": chat_id, "name": course_name[:128]}).encode('utf-8')
req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})

topic_id = None
try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode())
        if res.get("ok"):
            topic_id = res["result"]["message_thread_id"]
            print(f"Successfully created topic ID: {topic_id}")
        else:
            print(f"Failed to create topic: {res}")
except Exception as e:
    print(f"HTTP request failed: {e}")

# 2. Upload the files into the created topic using Telethon
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def main():
    await client.send_message(chat_id, f"📚 **{course_name}**\n\nUploading materials...", reply_to=topic_id)
    
    for root, dirs, files in os.walk(folder_path):
        for file in sorted(files): 
            if file.startswith('.'):
                continue
            file_path = os.path.join(root, file)
            print(f"Uploading {file}...")
            try:
                await client.send_file(chat_id, file_path, caption=f"🎬 {file}", reply_to=topic_id)
            except Exception as e:
                print(f"Failed to upload {file}: {e}")

with client:
    client.loop.run_until_complete(main())
