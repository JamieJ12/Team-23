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
