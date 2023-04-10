from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

# Timestamp to keep track of the last time the script was activated
last_activated = None

# Route to check if the bot is running and display the last activation time
@app.route('/')
def check_bot_status():
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

def run_web():
    if __name__ == '__main__':
       app.run(host='0.0.0.0')
    
