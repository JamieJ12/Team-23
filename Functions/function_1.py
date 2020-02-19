def dictionary_of_metrics(items):
    """
    Function calculates the mean, median, variance, standard deviation,
    minimum and maximum of the list of items.

    The input is a list of integers and it ouputs a dictionary.

    Arguments:

      items(list): list of intergers

    Returns:

      dictinary: with keys -- 'mean', 'median', 'std', 'var', 'min', and 'max',
      corresponding to the mean, median, standard deviation, variance,
      minimum and maximum of the input list

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

      >>>dictionary_of_metrics(gauteng)
      Output: {'mean': 26244.42,
             'median': 24403.5,
             'var': 108160153.17,
             'std': 10400.01,
             'min': 8842.0,
             'max': 39660.0}

    """
    #Create a numpy array np_items from items
    np_items = np.array(items)

    #Get mean,median,var,std,min and max using np_items
    mean = np.mean(np_items)
    median = np.median(np_items)
    var = np.var(np_items,ddof=1)
    std = np.std(np_items,ddof=1)
    mn = np.min(np_items)
    mx = np.max(np_items)

    #Return the appropriate Dictionary
    return {'mean': round(mean,2),
            'median': round(median,2),
            'var': round(var,2),
            'std': round(std,2),
            'min': round(mn,2),
            'max': round(mx,2)}
