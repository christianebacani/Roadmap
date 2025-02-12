# 1683.) Invalid Tweets
# Category : Pandas

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalidTweets = pd.DataFrame(columns=['tweet_id'])
    
    for _, row in tweets.iterrows():
        content = row.get('content')

        if len(content) > 15:
            invalidTweets = pd.concat([invalidTweets, pd.DataFrame({'tweet_id' : [row.get('tweet_id')]})], ignore_index=True)
    
    return invalidTweets