import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].apply(lambda x: len(x) > 15)][["tweet_id"]]