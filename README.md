# cat_on_lsd the mental FASTAI-CAT
Cat_On_LSD is an attempt at making humour with AI.

Since my cat died, I've decided to upload her consciousness. She was a total maniac. Here she is: https://twitter.com/cat_on_LSD

# ai-cat.py
Since I've implemented an AI model, Cat_On_LSD's tweets became way less random. For instance, when making a joke about Marx, it is very likely to make it about Capitalism. This is a consequence of retraining a model based on  Wikipedia.

# cat-bot.py 
This was used to generate a dataset to train cat-AI. This was used to finetune a much larger model based on Wikipedia.

About Data.json:
Please feel free to share ideas to expand this. It will feed a generator that I will use to train a model.

Structures are sentences with blank spaces such as :s: for subjects, :n: for nouns, :a: for actions, :l: for locations.

These sentences will be formed by swapping the above symbols with random elements from subjects, nouns, actions, and locations.
