# cat_on_lsd the mental FASTAI-CAT

Since my cat died, I've decided to upload her consciousness. She was a total maniac. Here she is: https://twitter.com/cat_on_LSD

# ai-cat.py
While posting with the cat-bot gave completely random tweets, the cat-AI can respect some patterns. For instance, when making a joke about Marx, it is very likely to make it about Capitalism.
This is a consequence of retraining a model based on  Wikipedia, using a dataset generated with the cat-bot.
Note: ai-cat.py at the moment isn't using any AI-model, it is just using a csv generated with an AI-model (cat-AI).

# cat-bot.py 
Some lines of code to generate random silly tweets. This was used to generate a dataset to train cat-AI.

About Data.json:
Please feel free to share ideas to enrich this.
Structures are sentences with blank spaces such as :s: for subjects, :n: for nouns, :a: for actions, :l: for locations.
These sentences will be formed by swapping the above symbols with random elements from subjects, nouns, actions, and locations.
