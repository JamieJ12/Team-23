# Add Imports
import numpy as np
import pandas as pd



# Function 1
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



# Function 2
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



# Function 3
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



# Function 4
def extract_municipality_hashtags(df):
    """The function inputs pandas dataframe and

    returns a modified dataframe that includes two new columns

    that contain information about the municipality and hashtag of the tweet.


    Arguments:

    The variable 'df' is the pandas input.

    With added column of extracted hashtags from each tweet

    using 'mun_dict' dictionary and inserts

    the result into a new column named 'municipality' in the same dataframe.

    """

    # Dictionary mapping official municipality twitter handles to the municipality name
    mun_dict = {
        '@CityofCTAlerts' : 'Cape Town',
        '@CityPowerJhb' : 'Johannesburg',
        '@eThekwiniM' : 'eThekwini' ,
        '@EMMInfo' : 'Ekurhuleni',
        '@centlecutility' : 'Mangaung',
        '@NMBmunicipality' : 'Nelson Mandela Bay',
        '@CityTshwane' : 'Tshwane'
        }
    #Get municipalities list of keys
    key = list(mun_dict.keys())

    # Add np.nan to all values for municipality column
    df["municipality"] = np.nan

    # Find tags corresponding to different municipalities and add them accordingly
    for k in key:
        df.loc[df["Tweets"].str.contains(k),"municipality"] = mun_dict[k]


    ######################################################

    # Make a list of all the Tweets with a #
    hashtags_tweets = list(df.loc[df["Tweets"].str.contains("#")]["Tweets"])

    # Get indices list of all the Tweets with a #
    index_hash = list(df.loc[df["Tweets"].str.contains("#")].index)

    # Isolate # words in each Tweet
    final = []
    for tweet in hashtags_tweets:
        tweet = tweet.split()

        hash_words = []
        for word in tweet:
            if word.startswith("#"):
                hash_words.append(word.lower())

        final.append(hash_words)

    # Add np.nan to all values for hashtags column
    df["hashtags"] = np.nan

    # Find indices corresponding to different Tweets and add hashtags accordingly
    df.loc[index_hash,"hashtags"] = final

    return df



# Function 5
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


# Function 6
def word_splitter(df):
    """

    The function splits the sentences in a dataframe's column into

    a list of the separate words.:

    Arguments:

    List is in the column named 'Splits Tweets'

    Fuction takes in dataframe in the column named 'Tweets'


    Returns a modified dataframe with a new column of a list of individual words

    """

    # Get Tweets from DataFrame
    tweets = df["Tweets"].to_list()

    # Split the Tweets into lowercase words
    split_tweets = [tweet.lower().split() for tweet in tweets]

    # Add Split Tweets to own column
    df["Split Tweets"] = split_tweets

    return df



# Function 7
def stop_words_remover(df):

    """
    Function removes english stop words from a tweet.


    Arguments:

    Fucntion takes in pandas dataframe

    It tokenises the sentences according to the definition in function 6


    Returns a modified dataframe with an added column of tweets without stopwords.

    """

    # dictionary of english stopwords
    stop_words_dict = {
        'stopwords':[
            'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
            'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
            'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
            'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
            'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
            'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
            'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
            'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
            'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
            'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
            'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
            'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
            'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
            'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
            'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
            'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
            'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
            'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
            "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
            'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
            'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
            'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
            'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
            'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
            'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
            'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
            'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
            'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
            'same', 'were', 'it', 'every', 'third', 'together'
        ]
    }
    # Get Tweets from DataFrame
    tweets = df["Tweets"].to_list()

    # Split Tweets into individual lowercase words
    split_tweets = [tweet.lower().split() for tweet in tweets]

    # Remove http and words in the stop words dictionary
    without_tweets = [[word for word in tweet if not(word in stop_words_dict["stopwords"])] for tweet in split_tweets]

    # Add Without Stop Words to own column
    df["Without Stop Words"] = without_tweets

    return df
