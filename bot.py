import os
from slack import WebClient
from slack.errors import SlackApiError
from pathlib import Path
from dotenv import load_dotenv
import schedule
import time

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# from apscheduler.schedulers.blocking import BlockingScheduler

# sched = BlockingScheduler({'apscheduler.timezone': 'UTC'})

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
# sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')


def sendMessage(client, text):
  # make the POST request through the python slack client
  #   print('hey: ', text)
  # check if the request was a success
  try:
    response = client.chat_postMessage(
        channel='#peer_group_11',
        text=text) #.get()
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

    # text="Good Morning! https://us04web.zoom.us/j/9731804632?pwd=cmwyVlRkTWQraGp3cVVQVmljakdVQT09"
    # sendMessage(client, text)
    # sched.start()

    # Runs from Monday to Friday at 5:30 (am) until 2014-05-30 00:00:00
    # sched.add_job(sendMessage(client, text), 'cron', day_of_week='mon-fri', hour=19, minute=51, end_date='2021-01-08')
    
    # schedule.every(20).seconds.do(sendMessage, client, text)
    schedule.every().monday.at("09:29").do(sendMessage, client, mon_text)
    schedule.every().tuesday.at("09:29").do(sendMessage, client, tue_text)
    schedule.every().wednesday.at("09:29").do(sendMessage, client, wed_text)
    schedule.every().thursday.at("09:29").do(sendMessage, client, thu_text)
    schedule.every().friday.at("09:29").do(sendMessage, client, fri_text)
    # schedule.every().day.at("09:33").do(sendMessage, client, mon_text)
    # schedule.every().monday.at("13:15").do(lambda: sendMessage(slack_client, text))
    # logging.info("entering loop")

    while True:
        schedule.run_pending()
        # schedule.next_run()
        time.sleep(60) # sleep for whatever seconds between checks on the scheduler