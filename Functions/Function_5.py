def number_of_tweets_per_day(df):

    # Isolate Date from DateTime Format
    df["Date"] = date_parser(df["Date"].to_list())

    #Set all Tweets to 1 so they can be counted
    df["Tweets"] = 1

    # Group By Date and Sum Tweets
    return df.groupby(["Date"]).sum()
