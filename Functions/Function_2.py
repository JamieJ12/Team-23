def five_num_summary(items):
    """
    The Function takes in a list of integers and returns a dictionary

    of the 5 number summary.

    Arguments:

      items (list): List of integers

    The function returns a dictionary with keys: 'max', 'median', 'min',

    'q1', and 'q3', corresponding to the maximum, median, minimum,

    first quartile and

    third quartile, respectively.

    Example:
    Input:
    >>>gauteng = [39660.0,
                  36024.0,
                  32127.0,
                  39488.0,
                  18422.0,
                  23532.0,
                  8842.0,
                  37416.0,
                  16156.0,
                  18730.0,
                  19261.0,
                  25275.0]

    >>>five_num_summary(gauteng)
    Output:
        {'max': 39660.0,
        'median': 24403.5,
        'min': 8842.0,
        'q1': 18653.0,
        'q3': 36372.0}

    """
    #Create a numpy array np_items from items
    np_items = np.array(items)

    #Get mean,median,var,std,min and max using np_items
    median = np.median(np_items)
    q1 = np.quantile(np_items, 0.25)
    q3 = np.quantile(np_items, 0.75)
    mn = np.min(np_items)
    mx = np.max(np_items)

    #Return the appropriate Dictionary
    return {'max': round(mx,2),
            'median': round(median,2),
            'min': round(mn,2),
            'q1': round(q1,2),
            'q3': round(q3,2),}
