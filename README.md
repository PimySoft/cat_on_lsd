# cat_on_lsd the mental cat-AI

Since my cat died, I've decided to upload her consciousness. She was a total maniac. Here she is: https://twitter.com/cat_on_LSD


# ai-cat.py
This picks from a csv file which sentences were generated with a cat-AI. The cat AI was trained with FastAI.
. FastAI makes it easy to retrain a model based on Wikipedia. This was done on a dataset of 300.000 sentences generated with cat-bot.py
. While posting with the cat-bot gave completely random tweets, the cat-AI can respect some patterns. For instance, when making a joke about Marx, it is very likely to make it about Capitalism.
. Fai-cat.py at the moment isn't using any AI-model. On PythonAnywhere it is just using a csv generated with an AI-model (cat-AI).

# cat-bot.py 
Some lines of code to generate random silly tweets. This was used to generate a dataset to train cat-AI.

#Data.json
. Please feel free to share ideas to enrich this.
. Structures are sentences with blank spaces such as :s: for subjects, :n: for nouns, :a: for actions, :l: for locations.
. These sentences will be formed by swapping the above symbols with random elements from subjects, nouns, actions, and locations.

#Posting to twitter
. There are 5 ways to post a tweet:
    To tweet a random follower: tweet_a_random_follower()
    To tweet a random follower: tweet_a_friend()
    To tweet without any mention: tweet()
    To find some notorious status about cats and reply: reply_to_a_notorious_status()
    To use any number of the above functions. This function has weights to make it a bit less likely to post to notorious tweets or followers:      post_random_type_of_tweet(int)
