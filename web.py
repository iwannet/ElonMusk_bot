from flask import Flask
from datetime import datetime
import pytz
from threading import Thread

app = Flask("")

# Timestamp to keep track of the last time the script was activated
last_activated = None

# Route to check if the bot is running and display the last activation time
@app.route('/')
def home():
    global last_activated
    if last_activated:
        tz = pytz.timezone('Europe/Brussels')
        last_activated = last_activated.astimezone(tz)
        last_activated_str = last_activated.strftime("%Y-%m-%d %H:%M:%S")
        message = f"If you see this, the bot is running. Source code available at https://github.com/iwannet/ElonMusk_bot.\n   Last comment (Belgium time): {last_activated_str}"
    else:
        message = "If you see this, the bot is running. Source code available at https://github.com/iwannet/ElonMusk_bot."
    last_activated = datetime.now()
    return message

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
