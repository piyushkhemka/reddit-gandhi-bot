from insults import insults_list
import config
import datetime
import praw
import random
import time


def authenticate():
    reddit = praw.Reddit(username=config.username,
                         password=config.password,
                         client_id=config.client_id,
                         client_secret=config.client_secret,
                         user_agent=config.user_agent)
    return reddit


def main():
    reddit = authenticate()
    subreddits = reddit.subreddit('all')

    # misspelling to make the bot angry
    ghandi = 'ghandi'

    insult_conclusion = " Just so you know, the correct spelling is [Gandhi](https://en.wikipedia.org/wiki/Mahatma_Gandhi)."

    print('Starting my watch\n')
    # for count, comment in enumerate(subreddits.stream.comments()):
    for comment in subreddits.stream.comments():
        # if count > 0 and count % 1000 == 0:
        #     print(f'{count}')
        if ghandi in comment.body.lower():
            try:
                insult_start = random.choice(insults_list)
                comment.reply(insult_start + insult_conclusion)
                print(f'Posted insult at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}. \n')
                time.sleep(60)
            except praw.exceptions.APIException as api:
                print(f'Got api exception. Going to sleep for 5 mins \n')
                time.sleep(60*12)
            except Exception as e:
                print(f'\nException = {e} \n')


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(f'\nException = {e} \n')
            time.sleep(60*20)
