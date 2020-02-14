### START FUNCTION
def stop_words_remover(df):

    # Get Tweets from DataFrame
    tweets = df["Tweets"].to_list()

    # Split Tweets into individual lowercase words
    split_tweets = [tweet.lower().split() for tweet in tweets]

    # Remove http and words in the stop words dictionary
    without_tweets = [[word for word in tweet if not(word in stop_words_dict["stopwords"])] for tweet in split_tweets]

    # Add Without Stop Words to own column
    df["Without Stop Words"] = without_tweets

    return df

### END FUNCTION
