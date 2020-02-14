### START FUNCTION
def extract_municipality_hashtags(df):

    #Get municipalities list of keys
    key = list(mun_dict.keys())

    # Add np.nan to all values for municipality column
    df["municipality"] = np.nan

    # find tags corresponding to different municipalities and add them accordingly
    for k in key:
        df.loc[df["Tweets"].str.contains(k),"municipality"] = mun_dict[k]


    ######################################################

    # Make a list of all the Tweets with a #
    hashtags_tweets = list(df.loc[df["Tweets"].str.contains("#")]["Tweets"])

    # Get indices list of all the Tweets with a #
    index_hash = list(df.loc[df["Tweets"].str.contains("#")].index)

    # Isolate # words in each Tweet
    final = []
    for tweet in hashtags_tweets:
        tweet = tweet.split()

        hash_words = []
        for word in tweet:
            if word.startswith("#"):
                hash_words.append(word.lower())

        final.append(hash_words)

    # Add np.nan to all values for hashtags column
    df["hashtags"] = np.nan

    # find indices corresponding to different Tweets and add hashtags accordingly
    df.loc[index_hash,"hashtags"] = final

    return df

### END FUNCTION
