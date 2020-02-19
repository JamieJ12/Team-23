def word_splitter(df):
    """

    The function splits the sentences in a dataframe's column into

    a list of the separate words.:

    Arguments:

    List is in the column named 'Splits Tweets'

    Fuction takes in dataframe in the column named 'Tweets'


    Returns a modified dataframe with a new column of a list of individual words

    """

    # Get Tweets from DataFrame
    tweets = df["Tweets"].to_list()

    # Split the Tweets into lowercase words
    split_tweets = [tweet.lower().split() for tweet in tweets]

    # Add Split Tweets to own column
    df["Split Tweets"] = split_tweets

    return df
