def number_of_tweets_per_day(df):

    """

    The function calculates the number of tweets that were posted per day.

    Arguments: The variable 'df' is the pandas input.

    Returns: df
    The index of the new dataframe is 'Date' in the format:'yyyy-mm-dd',
    and the column of the new dataframe is 'Tweets',
    corresponding to the date and number of tweets, respectively.
    The functiion returns the number of tweets per day.

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

    >>>number_of_tweets_per_day(twitter_df.copy())
    Output
                Tweets
    Date
    2019-11-20	18
    2019-11-21	11
    2019-11-22	25
    2019-11-23	19
    2019-11-24	14
    2019-11-25	20
    2019-11-26	32
    2019-11-27	13
    2019-11-28	32
    2019-11-29	16

    """

    # Isolate Date from DateTime Format
    df["Date"] = date_parser(df["Date"].to_list())

    #Set all Tweets to 1 so they can be counted
    df["Tweets"] = 1

    # Group By Date and Sum Tweets
    return df.groupby(["Date"]).sum()
