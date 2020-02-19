def date_parser(dates):
    """

    The Function inputs a list of date-time strings formatted as:

        'yyyy-mm-dd hh:mm:ss'

        The format : 'yyyy-mm-dd' represents the date and

        The format: 'hh:mm:ss' represents the time

    The function returns a:

    list of strings where each element in the returned list contains

    only the date in the 'yyyy-mm-dd' format.


    """
    # Split DateTime and Isolate Date
    return [date.split()[0] for date in dates]
