def extract_municipality_hashtags(df):
    """The function inputs pandas dataframe and

    returns a modified dataframe that includes two new columns

    that contain information about the municipality and hashtag of the tweet.


    Arguments:

    The variable 'df' is the pandas input.

    With added column of extracted hashtags from each tweet

    using 'mun_dict' dictionary and inserts

    the result into a new column named 'municipality' in the same dataframe.

    """

    # Dictionary mapping official municipality twitter handles to the municipality name
    mun_dict = {
        '@CityofCTAlerts' : 'Cape Town',
        '@CityPowerJhb' : 'Johannesburg',
        '@eThekwiniM' : 'eThekwini' ,
        '@EMMInfo' : 'Ekurhuleni',
        '@centlecutility' : 'Mangaung',
        '@NMBmunicipality' : 'Nelson Mandela Bay',
        '@CityTshwane' : 'Tshwane'
        }
    #Get municipalities list of keys
    key = list(mun_dict.keys())

    # Add np.nan to all values for municipality column
    df["municipality"] = np.nan

    # Find tags corresponding to different municipalities and add them accordingly
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

    # Find indices corresponding to different Tweets and add hashtags accordingly
    df.loc[index_hash,"hashtags"] = final

    return df
