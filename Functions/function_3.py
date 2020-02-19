def date_parser(dates):
    """

    The Function inputs a

    Arguments:
        dates (list): list of date-time strings formatted as:
                'yyyy-mm-dd hh:mm:ss'
        The format : 'yyyy-mm-dd' represents the date and
        The format: 'hh:mm:ss' represents the time

    The function returns a:list of strings where each element in the
    returned list contains only the date in the 'yyyy-mm-dd' format.

    Examples:
    Prerequites:
    >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
    >>> twitter_df = pd.read_csv(twitter_url)
    >>> dates = twitter_df['Date'].to_list()

    Example 1:
    Input:
    >>> dates[:3]
    ['2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10']
    
    >>>date_parser(dates[:3])
    Output: ['2019-11-29', '2019-11-29', '2019-11-29']

    Example 2:
    Input:
    >>>dates[-3:]
    ['2019-11-20 10:07:59',
    '2019-11-20 10:07:41',
    '2019-11-20 10:00:09']

    >>>date_parser(dates[-3:])
    Output:['2019-11-20', '2019-11-20', '2019-11-20']

    """
    # Split DateTime and Isolate Date
    return [date.split()[0] for date in dates]
