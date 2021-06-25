import json
import tweepy
import random
import time
import pandas as pd
import numpy as np

# Authenticate to Twitter
API_Key = "YOUR KEY"
API_Secret_Key = "YOUR KEY"
Access_Token_Key = "YOUR KEY"
Secret_Access_Token = "YOUR KEY"
auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
auth.set_access_token(Access_Token_Key, Secret_Access_Token)
api = tweepy.API(auth)
my_screen_name = "cat_on_LSD"

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

structures_list = []
subjects_list = []
nouns_list = []
actions_list = []
locations_list = []

with open('data.json', 'r') as data_file:
    data = json.load(data_file)
    structures_list = data['structures']
    subjects_list = data['subjects']
    nouns_list = data['nouns']
    actions_list = data['actions']
    locations_list = data['locations']

def random_sentence(user_screen_name=" "):
    random_index = random.randint(0, len(structures_list))
    current_structure_list = structures_list[random_index-1].split(" ")
    user_to_talk_to = user_screen_name
    for index in range(0, len(current_structure_list)):
        if current_structure_list[index] == ':s:':
            if user_to_talk_to == " ":
                current_structure_list[index] = return_subject()
            else:
                current_structure_list[index] = f"@{user_to_talk_to}"
                user_to_talk_to = " "
        if current_structure_list[index] == ':n:':
            current_structure_list[index] = return_noun()
        if current_structure_list[index] == ':a:':
            current_structure_list[index] = return_action()
        if current_structure_list[index] == ':l:':
            current_structure_list[index] = return_location()
    try:
        if current_structure_list[0][0].isupper() == False and current_structure_list[0][0] != "#" and current_structure_list[0][0] != " ":
            print(current_structure_list[0][0])
            current_structure_list[0][0] = current_structure_list[0][0].capitalize()
    except:
        pass

    return current_structure_list

def listToString(string):
    str = " "
    return (str.join(string))

def return_subject():
    random_index = random.randint(0, len(subjects_list))
    sub = subjects_list[random_index-1]
    return sub

def return_noun():
    random_index = random.randint(0, len(nouns_list))
    noun = nouns_list[random_index-1]
    return noun

def return_action():
    random_index = random.randint(0, len(actions_list))
    action = actions_list[random_index-1]
    return action

def return_location():
    random_index = random.randint(0, len(locations_list))
    location = locations_list[random_index-1]
    return location

def return_a_top_x_tweet_data(keyword, tweets_to_return):
    tweet_status = api.search(q=keyword, tweet_mode='extended', result_type='popular', count=tweets_to_return) #This won't return a Dict to browse, but a Status
    #convert one of the above statuses to string
    index = random.randint(0, tweets_to_return-1)
    json_str = json.dumps(tweet_status[index]._json)
    #deserialise string into python object
    parsed = json.loads(json_str)
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    #print(parsed['full_text'])
    return({'text': parsed['full_text'], 'name': parsed['user']['name'], 'screen_name': parsed['user']['screen_name'], 'tweet_id': parsed['id']})

def reply_to_a_notorious_status():
    tweet = listToString(random_sentence())
    tweet_data = return_a_top_x_tweet_data('#cat', 3)
    print(f"@{tweet_data['screen_name']} The thing is, {tweet}", tweet_data['tweet_id'])
    #api.update_status(f"@{tweet_data['screen_name']} The thing is, {tweet}", tweet_data['tweet_id'])

# NOTE :rfl: could stand for Random Follower to use in sentences
# Retrive followers list and pick a random one.
def tweet_a_random_follower():
    tweet = " "
    my_followers_list = api.followers(my_screen_name)
    index = random.randint(0, len(my_followers_list)-1)
    follower = my_followers_list[index].screen_name
    while follower not in tweet:
        tweet = listToString(random_sentence(follower))
    print(tweet)
    #api.update_status(tweet)

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

def tweet_a_friend():
    tweet = " "
    my_followed_list = get_friends(my_screen_name)
    index = random.randint(0, len(my_followed_list) - 1)
    friend = my_followed_list[index].screen_name
    while friend not in tweet:
        tweet = listToString(random_sentence(friend))
    print(tweet)
    #api.update_status(tweet)

def tweet(b):
    a = 0
    list_of_tweets = []
    while a < b:
        tweet = listToString(random_sentence())
        list_of_tweets.append(tweet)
        a+=1
        print(tweet)
    generate_training_csv(list_of_tweets)


    #api.update_status(tweet)

def post_random_type_of_tweet(times):
    while times > 0:
        n = random.randint(1, 10)
        if n < 5:
            tweet(1)
        if 5 <= n < 9:
            tweet_a_random_follower()
        if n == 9:
            reply_to_a_notorious_status()
        if n == 10:
            tweet_a_friend()
        times -= 1
        time.sleep(2)

def generate_training_csv(list_of_tweets):
    np_array = np.asarray(list_of_tweets)
    DF = pd.DataFrame(np_array)
    DF.to_csv("lsd_cat_trainint_set.csv")

#post_random_type_of_tweet(10)
#tweet_a_random_follower()
#tweet_a_friend()
tweet(10)
#reply_to_a_notorious_status()





