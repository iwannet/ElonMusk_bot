import praw
import os
import time
import random
import subprocess


def stop_web():
    subprocess.run(["pkill", "-f", "web.py"])


def start_web():
    subprocess.Popen(["python3", "web.py"])

answer_list = [
  "You're fired",
  "$8 please",
  "I've laid off most of the staff, and Twitter's still running. Looks like they weren't necessary.",
  "You look stupid. Fired.",
  "If you really love the company, you should be willing to work here for free.",
  "You're fired, now pay me $8",
  "I only bought twitter so i wouldnt get bullied anymore",
  "What do you mean, You cant work 80 hours a week ?",
  "Why have you only written 69 lines of code today?",
  "What do you mean: you couldnt code your way out of a paper bag?",
  "Disagreeing with me is counterproductive. Fired.",
  "I think i am going to buy reddit",
  "The secret to success is to fail fast and learn from your mistakes.",
  "I don't care about your feelings. I care about facts and logic.",
  "The best way to predict the future is to invent it.",
  "Don't let anyone tell you what you can or can't do. Unless it's me.",
  "I'm not a billionaire. I'm a visionary.",
  "The only thing that matters is innovation. And memes.",
  "There is no such thing as a bad idea. Except yours.",
  "Twitter is my personal diary.",
  "I dont follow anyone on twitter because I dont need their opinions.",
  "Twitter is the best place to test my ideas and see how people react.",
  "Sometimes I tweet just to mess with people's minds.",
  "Twitter is like a game for me. The more likes and retweets I get, the more points I score.",
  "Twitter is where I announce my plans for world domination."
]

trigger_list = [
  "Elon Musk", "elon musk", "Elon musk", "Elon Tusk", "elon tusk",
  "Space Karen", "space karen", "u/ElonMusk_bot", "elon-bot", "twitter",
  "Twitter", "elon"
]

sub = "ProgrammerHumor"


def bot_login():
  reddit = praw.Reddit(client_id="",
                       client_secret="",
                       username="",
                       password="",
                       user_agent="")
  return reddit


def run_bot(reddit, comments_replied_to):

  print("Searching last 1,000 comments") 

  for comment in reddit.subreddit(sub).comments(limit=1000):
    res = any(ele in comment.body for ele in trigger_list)

    if res == True and comment.id not in comments_replied_to and comment.author != reddit.user.me(
    ):
      print("String with trigger found in comment " + comment.id + "\n")

      answer = random.choice(answer_list)
      comment.reply(answer)

      print("Replied to comment " + comment.id + "\n" + answer)

      comments_replied_to.append(comment.id)

      with open("comments_replied_to.txt", "a") as f:
        f.write(comment.id + "\n")

        sleep()
        stop_web()
        time.sleep(1)
        start_web()

    else:
      print("No Comment found, restarting")
      stop_web()
      time.sleep(1)
      start_web()

  print("\nSearch Completed.")

  print(comments_replied_to)


def sleep():
  print("\nSleeping for 10 min...")

  time.sleep(600)


def get_saved_comments():
  if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
  else:
    with open("comments_replied_to.txt", "r") as f:
      comments_replied_to = f.read()
      comments_replied_to = comments_replied_to.split("\n")
      comments_replied_to = [_f for _f in comments_replied_to if _f]

  return comments_replied_to




reddit = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)


while True:
         run_bot(reddit, comments_replied_to)
