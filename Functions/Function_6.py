### START FUNCTION
def word_splitter(df):

    # Get Tweets from DataFrame
    tweets = df["Tweets"].to_list()

    # Split the Tweets into lowercase words
    split_tweets = [tweet.lower().split() for tweet in tweets]

    # Add Split Tweets to own column
    df["Split Tweets"] = split_tweets

    return df

### END FUNCTION
