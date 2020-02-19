def number_of_tweets_per_day(df):

    """

    The function calculates the number of tweets that were posted per day.

    Arguments:

    The index of the new dataframe is 'Date' in the format:

        'yyyy-mm-dd',

    and the column of the new dataframe is 'Tweets',

    corresponding to the date and number of tweets, respectively.

    The functiion returns the number of tweets per day.


    """

    # Isolate Date from DateTime Format
    df["Date"] = date_parser(df["Date"].to_list())

    #Set all Tweets to 1 so they can be counted
    df["Tweets"] = 1

    # Group By Date and Sum Tweets
    return df.groupby(["Date"]).sum()
