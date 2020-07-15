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

subreddits = reddit.subreddit('all')

# misspelling to make the bot angry
ghandi = 'ghandi'

insult_conclusion = " The correct spelling is [Gandhi](https://en.wikipedia.org/wiki/Mahatma_Gandhi)."

print('Starting my watch. Will occasionally print count of posts I have monitored so far\n')
for count, comment in enumerate(subreddits.stream.comments()):
    if count > 0 and count % 1000 == 0:
        print(f'{count}')
    if ghandi in comment.body.lower():
        try:
            insult_start = random.choice(insults_list)
            comment.reply(insult_start + insult_conclusion)
            print(f'Posted insult at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}. \n')
            time.sleep(60)
        except praw.exceptions.APIException as api:
            print(f'Got api exception. Going to sleep for 5 mins \n')
            time.sleep(600)
        except Exception as e:
            print(f'\nException = {e} \n')
            