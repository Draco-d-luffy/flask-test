import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)
slack_event_api = SlackEventAdapter('e435a3403c117be73a76c7588aa5aaaa' , '/slack/events', app)
#k
if __name__ == "__main__":
    app.run(debug=True)
