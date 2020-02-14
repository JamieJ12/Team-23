### START FUNCTION
def dictionary_of_metrics(items):

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

### END FUNCTION
