# cat_on_lsd
Since my cat died, I've decided to upload her consciousness.


. In the data.json, structures are sentences with blank spaces such as :s: for subjects, :n: for nouns, /:a: for actions, :l: for locations.
. These sentences will be formed by swapping the above symbols with random elements from subjects, nouns, actions, and locations.
. There are 5 ways to post a tweet:
    To tweet a random follower: tweet_a_random_follower()
    To tweet a random follower: tweet_a_friend()
    To tweet without any mention: tweet()
    To find some notorious status about cats and reply: reply_to_a_notorious_status()
    To use any number of the above functions. This function has weights to make it a bit less likely to post to notorious tweets or followers:      post_random_type_of_tweet(int)
