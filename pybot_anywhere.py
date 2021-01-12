import os
import sys
from slack import WebClient
from slack.errors import SlackApiError
from pathlib import Path
from dotenv import load_dotenv
import schedule
import time
from datetime import datetime

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def sendMessage(client, text):
  try:
    response = client.chat_postMessage(
        channel='#peer_group_11',
        text=text) #.get()
    print("message posted in slack")
    # assert response["message"]["text"] == text
  except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")

if __name__ == "__main__":
    client = WebClient(token = os.environ['SLACK_TOKEN'])
    mon_text="<https://us04web.zoom.us/j/79155939455?pwd=Z3BhcHFLa0c0NU5uUW5ST01pa3QzZz09|*Goal Setting Day*> <!here|here> \n Lambda recommends the 10-10-10 framework for weekly job search goals.  10 quality applications, 10 outreach messages, and 10 technical challenges.  As you look ahead to everything you have going on this week share with the group... \n\n• In the past week, how many applications, outreach messages, and challenges did you execute? \n• If you fulfilled the weekly 10-10-10 goals, how did you ensure you hit them? Share tips with the group. \n• If you didn’t, identify blockers that prevent you from hitting the goals. How can you become unblocked? \n• How will you execute or adjust the 10-10-10 goals to fit your individual job search this week? Take into consideration what you have going on this week, interviews you may need to prep for, take home challenges, etc."
    tue_text="<https://us04web.zoom.us/j/78965763211?pwd=aXN0c0lYWnh6bmt5VHBUSjMwM2NWQT09|*Networking*> <!here|here> \nOn average, 70% of jobs are found through networking. When we checked in with hired Lambda School alumni, we found that 87% credited networking to their hired success. With these stats, it’s undeniable how important networking is.\n\nAs time permits, have one to two group members pull up a networking message they sent in the last week.\n\nIf the message has not received a response, what is a way to reword the message for more success in future attempts? Take a moment to collectively figure out a way to follow-up on the message that has already been sent out.\n\nIf this message has received a response, what do you think prompted the individual to reply? Is there a part of the message other group members can incorporate into their own outreach attempts?"
    wed_text="<https://us04web.zoom.us/j/79733526816?pwd=aGs1aDZmdGJGaDBlLzFCOHhHTUV6Zz09|*Networking*> <!here|here> \nOn average, 70% of jobs are found through networking. When we checked in with hired Lambda School alumni, we found that 87% credited networking to their hired success. With these stats, it’s undeniable how important networking is.\n\nAs time permits, have one to two group members pull up a networking message they sent in the last week.\n\nIf the message has not received a response, what is a way to reword the message for more success in future attempts? Take a moment to collectively figure out a way to follow-up on the message that has already been sent out.\n\nIf this message has received a response, what do you think prompted the individual to reply? Is there a part of the message other group members can incorporate into their own outreach attempts?"
    thu_text="<https://us04web.zoom.us/j/77776092342?pwd=eHJLamMyL1hyOEtlSzI3dlRjaHo4dz09|*Technical Challenges*> <!here|here> \nToday, have each group member share what coding challenges or technical work they have engaged with this week to meet the goal of 10 weekly coding challenges. As applicable, discuss the following questions:\n\nWhat support, if any, do you need technically? Are there certain technical skills, a project, or a challenge that has you stuck? Share so the group can help you!\n\nWhat challenges, methods or platforms are you choosing to practice your technical skills? How are these preparing you for future technical interviews?\n\nAre you checking the skills on applications to ensure you practice qualifying skills?"
    fri_text="<https://us04web.zoom.us/j/75761029694?pwd=dGhhd0RzUmpnbDFzYVhEMjdSS0RsQT09|*Weekly Wrap Up*> <!here|here> \nTime to close out the week! Let’s talk highs and lows.\n\nWhat was one successful or win moment you experienced this week? OR something you’re grateful for about your current experience/week? Infuse a little positivity into your job search?\n\nWhat was a low you experienced this week?\n\nIf you overcame it, how do you push through?\n\nIf you’re still trying to deal, how can the group support you (if applicable)? How do you see yourself pushing past this?"
    text="testing scheduled scripts with pythonanywhere"
    day=datetime.today().strftime('%A')

    switcher = {
        "Monday": mon_text,
        "Tuesday": tue_text,
        "Wednesday": wed_text,
        "Thursday": thu_text,
        "Friday": fri_text
    }

    if day in switcher:
        sendMessage(client, switcher[day])

    sys.exit(f"Successfully sent a message in slack on {day}")