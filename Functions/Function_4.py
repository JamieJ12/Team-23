def extract_municipality_hashtags(df):
    """
    The function inputs pandas dataframe and
    returns a modified dataframe that includes two new columns
    that contain information about the municipality and hashtag of the tweet.


    Arguments:
    The variable 'df' is the pandas input.

    Returns:
    df with added column of extracted hashtags from each tweet
    using 'mun_dict' dictionary and inserts the result into a new column
    named 'municipality' in the same dataframe.

    Example:
    Prerequites:
    >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
    >>> twitter_df = pd.read_csv(twitter_url)

    Inputs:
    >>>twitter_df.copy().head()

        Tweets	                                            Date
    0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54
    1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
    2	@BongaDlulane Query escalated to media desk.	     2019-11-29 12:46:10
    3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43


    >>>extract_municipality_hashtags(twitter_df.copy())
    Output
    	Tweets	                                            Date	            municipality	hashtags
    0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	NaN	            NaN
    1	@saucy_mamiie Pls log a call on 0860037566	2019-11-29 12:46:53	NaN	NaN
    2	@BongaDlulane Query escalated to media desk.	2019-11-29 12:46:10	NaN	NaN
    3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	NaN	            NaN
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	NaN	            [#eskomfreestate, #mediastatement]
    ...	...	...	...	...
    195	Eskom's Visitors Centres’ facilities include i...	2019-11-20 10:29:07	NaN	            NaN
    196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	NaN	            [#eskom, #eskom, #poweringyourworld]
    197	@ArthurGodbeer Is the power restored as yet?	2019-11-20 10:07:59	NaN	NaN
    198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	NaN	            NaN
    199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	NaN	            NaN

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
