import tweepy
import pandas as pd
import time
import random
import json
# Authenticate to Twitter
API_Key = ""
API_Secret_Key = ""
Access_Token_Key = ""
Secret_Access_Token = ""
auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
auth.set_access_token(Access_Token_Key, Secret_Access_Token)
api = tweepy.API(auth)
my_screen_name = "cat_on_LSD"

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

ROW_NUMBER = 0
def generate_tweet():
    tweet = ""
    df = pd.read_csv('cat-AI-tweets.csv')
    try:
        tweet = df.text[ROW_NUMBER]
        df = df.drop(df.index[ROW_NUMBER])
        df.to_csv("cat-AI-tweets.csv", index=False)
    except:
        print("Out of AI tweets in the csv")

    return(tweet)

def return_a_top_x_tweet_data(keyword, tweets_to_return):
    tweet_status = api.search(q=keyword, tweet_mode='extended', result_type='popular', count=tweets_to_return) #This won't return a Dict to browse, but a Status
    index = random.randint(0, tweets_to_return-1)
    json_str = json.dumps(tweet_status[index]._json)
    parsed = json.loads(json_str)
    return({'text': parsed['full_text'], 'name': parsed['user']['name'], 'screen_name': parsed['user']['screen_name'], 'tweet_id': parsed['id']})

def get_friends(user_name):
    api = tweepy.API(auth)
    friends = []
    for page in tweepy.Cursor(api.friends, screen_name=user_name, wait_on_rate_limit=True).pages():
        try:
            friends.extend(page)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    return friends

def tweet_a_random_follower():
    my_followers_list = api.followers(my_screen_name)
    index = random.randint(0, len(my_followers_list)-1)
    follower = my_followers_list[index].screen_name
    tweet = follower + " I was thinking..." + generate_tweet()
    return(tweet)

def reply_to_a_notorious_status():
    tweet = generate_tweet()
    tweet_data = return_a_top_x_tweet_data('#cat', 3)
    return(f"@{tweet_data['screen_name']} The thing is, {tweet}", tweet_data['tweet_id'])

def tweet_a_friend():
    my_followed_list = get_friends(my_screen_name)
    index = random.randint(0, len(my_followed_list) - 1)
    friend = my_followed_list[index].screen_name
    tweet = friend + " so... " + generate_tweet()
    return(tweet)

def post_random_type_of_tweet(times):
    while times > 0:
        n = random.randint(1, 10)
        if n < 5:
            api.update_status(generate_tweet())
        if 5 <= n < 9:
            api.update_status(tweet_a_random_follower())
        if n == 9:
            api.update_status(reply_to_a_notorious_status())
        if n == 10:
            api.update_status(tweet_a_friend())
        times -= 1
        time.sleep(1200)

post_random_type_of_tweet(4)

