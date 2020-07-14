from insults import insults_list
import config
import datetime
import praw
import random
import time

reddit = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent)

print(reddit.user.me())

subreddits = reddit.subreddit('test_gandhi_bot')



print(subreddits)

# phrase to make the bot angry
ghandi = 'ghandi'

insult_conclusion = " The correct spelling is [Gandhi](https://en.wikipedia.org/wiki/Mahatma_Gandhi)."


for comment in subreddits.stream.comments():
    print(comment.body.lower())
    if ghandi in comment.body.lower():
        try:
            insult_start = random.choice(insults_list)
            comment.reply(insult_start + insult_conclusion)
            print(f'Posted insult at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} \n')
            time.sleep(100)
        except praw.exceptions.APIException as api:
            print(f'Got api exception. Going to sleep for 5 mins \n')
            time.sleep(600)
        except Exception as e:
            print(f'Exception = {e} \n')
            