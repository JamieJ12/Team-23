### START FUNCTION
def five_num_summary(items):

    #Create a numpy array np_items from items
    np_items = np.array(items)

    #Get mean,median,var,std,min and max using np_items
    median = np.median(np_items)
#     q1 = np.percentile(np_items,25,interpolation = 'midpoint')
#     q3 = np.percentile(np_items,75,interpolation = 'midpoint')
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

### END FUNCTION
