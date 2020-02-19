def word_splitter(df):
    """

    The function splits the sentences in a dataframe's column into

    a list of the separate words.:

    Arguments: The variable 'df' is the pandas input.

    Returns: df with the added column named 'Splits Tweets'


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


    >>>word_splitter(twitter_df.copy())
    Output
        Tweets	                                            Date	            Split Tweets
    0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	[@bongadlulane, please, send, an, email, to, m...
    1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53	[@saucy_mamiie, pls, log, a, call, on, 0860037...
    2	@BongaDlulane Query escalated to media desk.	    2019-11-29 12:46:10	[@bongadlulane, query, escalated, to, media, d...
    3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	[before, leaving, the, office, this, afternoon...
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	[#eskomfreestate, #mediastatement, :, eskom, s...
    ...	...	...	...
    195	Eskom's Visitors Centresâ€™ facilities include i...	2019-11-20 10:29:07	[eskom's, visitors, centresâ€™, facilities, incl...
    196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	[#eskom, connected, 400, houses, and, in, the,...
    197	@ArthurGodbeer Is the power restored as yet?	    2019-11-20 10:07:59	[@arthurgodbeer, is, the, power, restored, as,...
    198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	[@muthambipaulina, @sabcnewsonline, @iol, @enc...
    199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	[rt, @gp_dhs:, the, @gautengprovince, made, a,...
    """

    # Get Tweets from DataFrame
    tweets = df["Tweets"].to_list()

    # Split the Tweets into lowercase words
    split_tweets = [tweet.lower().split() for tweet in tweets]

    # Add Split Tweets to own column
    df["Split Tweets"] = split_tweets

    return df
