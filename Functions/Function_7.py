def stop_words_remover(df):

    """
    Function removes english stop words from a tweet.


    Arguments: The variable 'df' is the pandas input.
    Function takes in pandas dataframe


    Returns:df, a modified dataframe with an added column of tweets without stopwords.

    Example:
    Prerequites:
    >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
    >>> twitter_df = pd.read_csv(twitter_url)

    Inputs:
    >>>twitter_df.copy().head()

        Tweets	                                            Date
    0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54
    1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
    2	@BongaDlulane Query escalated to media desk.	     2019-11-29 12:46:10
    3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43

    >>>stop_words_remover(twitter_df.copy())
    Output
    	Tweets	                                            Date	            Without Stop Words
    0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	[@bongadlulane, send, email, mediadesk@eskom.c...
    1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53	[@saucy_mamiie, pls, log, 0860037566]
    2	@BongaDlulane Query escalated to media desk.	    2019-11-29 12:46:10	[@bongadlulane, query, escalated, media, desk.]
    3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	[leaving, office, afternoon,, heading, weekend...
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	[#eskomfreestate, #mediastatement, :, eskom, s...
    ...	...	...	...
    195	Eskom's Visitors Centres’ facilities include i...	2019-11-20 10:29:07	[eskom's, visitors, centres’, facilities, incl...
    196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	[#eskom, connected, 400, houses, process, conn...
    197	@ArthurGodbeer Is the power restored as yet?	    2019-11-20 10:07:59	[@arthurgodbeer, power, restored, yet?]
    198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	[@muthambipaulina, @sabcnewsonline, @iol, @enc...
    199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	[rt, @gp_dhs:, @gautengprovince, commitment, e...
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
