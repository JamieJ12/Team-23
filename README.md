# Team-23---Analyze PREDICT ESKOM
This package was created to analyze data from ESKOM
The role was to build 7 functions using python which will need to process both numeric and text data.

## Functions

### Function_1
Function calculates the mean, median, variance, standard deviation,
  minimum and maximum of the list of items.

  The input is a list of integers and it outputs a dictionary.

  Arguments:

    items(list): list of integers

  Returns:

    dictionary: with keys -- 'mean', 'median', 'std', 'var', 'min', and 'max',
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



### Function_2
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


### Function_3
The Function inputs a

  Arguments:
      dates (list): list of date-time strings formatted as:
              'yyyy-mm-dd hh:mm:ss'
      The format : 'yyyy-mm-dd' represents the date and
      The format: 'hh:mm:ss' represents the time

  The function returns a:list of strings where each element in the
  returned list contains only the date in the 'yyyy-mm-dd' format.

  Examples:
  Prequites:
  ```bash
  >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
  >>> twitter_df = pd.read_csv(twitter_url)
  >>> dates = twitter_df['Date'].to_list()
  ```

  Example 1:
  Input:
  ```bash
  >>> dates[:3]
  ['2019-11-29 12:50:54',
  '2019-11-29 12:46:53',
  '2019-11-29 12:46:10']

  >>>date_parser(dates[:3])
  Output: ['2019-11-29', '2019-11-29', '2019-11-29']
  ```

  Example 2:
  Input:
  ```bash
  >>>dates[-3:]
  ['2019-11-20 10:07:59',
  '2019-11-20 10:07:41',
  '2019-11-20 10:00:09']

  >>>date_parser(dates[-3:])
  Output:['2019-11-20', '2019-11-20', '2019-11-20']
  ```



### Function_4
The function inputs pandas dataframe and
  returns a modified dataframe that includes two new columns
  that contain information about the municipality and hashtag of the tweet.


  Arguments:
  The variable 'df' is the pandas input.

  Returns:
  df with added column of extracted hashtags from each tweet
  using 'mun_dict' dictionary and inserts the result into a new column
  named 'municipality' in the same dataframe.

  Example:
  Prerequites:
  ```bash
  >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
  >>> twitter_df = pd.read_csv(twitter_url)
  ```
  Inputs:
  ```bash
  >>>twitter_df.copy().head()

      Tweets	                                           Date
  0	@BongaDlulane Please send an email to mediades...	    2019-11-29 12:50:54
  1	@saucy_mamiie Pls log a call on 0860037566	          2019-11-29 12:46:53
  2	@BongaDlulane Query escalated to media desk.	        2019-11-29 12:46:10
  3	Before leaving the office this afternoon, head...	    2019-11-29 12:33:36
  4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	    2019-11-29 12:17:43


  >>>extract_municipality_hashtags(twitter_df.copy())
  ```
  Output
  ```bash
            Tweets	                 Date	municipality	hashtags
  0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	NaN	NaN
  1	@saucy_mamiie Pls log a call on 0860037566	               2019-11-29 12:46:53	NaN	NaN
  2	@BongaDlulane Query escalated to media desk.	               2019-11-29 12:46:10	NaN	NaN
  3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	NaN	NaN
  4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	NaN	[#eskomfreestate, #mediastatement]
  ...	...	...	...	...
  195	Eskom's Visitors Centres’ facilities include i...	2019-11-20 10:29:07	NaN	NaN
  196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	NaN	[#eskom, #eskom, #poweringyourworld]
  197	@ArthurGodbeer Is the power restored as yet?	               2019-11-20 10:07:59	NaN	NaN
  198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	NaN	NaN
  199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	NaN	NaN
  ```


### Function_5
The function calculates the number of tweets that were posted per day.

  Arguments: The variable 'df' is the pandas input.

  Returns: df
  The index of the new dataframe is 'Date' in the format:'yyyy-mm-dd',
  and the column of the new dataframe is 'Tweets',
  corresponding to the date and number of tweets, respectively.
  The functiion returns the number of tweets per day.

  Example:
  ```bash
  Prerequites:
  >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
  >>> twitter_df = pd.read_csv(twitter_url)
  ```

  Inputs:
  ```bash
  >>>twitter_df.copy().head()

      Tweets	                                        Date
  0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54
  1	@saucy_mamiie Pls log a call on 0860037566	      2019-11-29 12:46:53
  2	@BongaDlulane Query escalated to media desk.	    2019-11-29 12:46:10
  3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36
  4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43

  >>>number_of_tweets_per_day(twitter_df.copy())
  Output
              Tweets
  Date
  2019-11-20	18
  2019-11-21	11
  2019-11-22	25
  2019-11-23	19
  2019-11-24	14
  2019-11-25	20
  2019-11-26	32
  2019-11-27	13
  2019-11-28	32
  2019-11-29	16
  ```

### Function_6
The function splits the sentences in a dataframe's column into

  a list of the separate words.:

  Arguments: The variable 'df' is the pandas input.

  Returns: df with the added column named 'Splits Tweets'


  Example:
  Prerequites:
  ```bash
  >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
  >>> twitter_df = pd.read_csv(twitter_url)
  ```
  Inputs:
  ```bash
  >>>twitter_df.copy().head()

      Tweets	                                            Date
  0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54
  1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
  2	@BongaDlulane Query escalated to media desk.	     2019-11-29 12:46:10
  3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36
  4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43


  >>>word_splitter(twitter_df.copy())
  Output
      Tweets	                                        Date	            Split Tweets
  0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	[@bongadlulane, please, send, an, email, to, m...
  1	@saucy_mamiie Pls log a call on 0860037566	      2019-11-29 12:46:53	[@saucy_mamiie, pls, log, a, call, on, 0860037...
  2	@BongaDlulane Query escalated to media desk.	    2019-11-29 12:46:10	[@bongadlulane, query, escalated, to, media, d...
  3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	[before, leaving, the, office, this, afternoon...
  4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	[#eskomfreestate, #mediastatement, :, eskom, s...
  ...	...	...	...
  195	Eskom's Visitors Centresâ€™ facilities include i...	2019-11-20 10:29:07	[eskom's, visitors, centresâ€™, facilities, incl...
  196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	[#eskom, connected, 400, houses, and, in, the,...
  197	@ArthurGodbeer Is the power restored as yet?	    2019-11-20 10:07:59	[@arthurgodbeer, is, the, power, restored, as,...
  198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	[@muthambipaulina, @sabcnewsonline, @iol, @enc...
  199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	[rt, @gp_dhs:, the, @gautengprovince, made, a,...
  ```

### Function_7
Function removes english stop words from a tweet.

  Arguments: The variable 'df' is the pandas input.
  Function takes in pandas dataframe

  Returns:df, a modified dataframe with an added column of tweets without stopwords.

  Example:
  Prerequites:
  ```bash
  >>> twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
  >>> twitter_df = pd.read_csv(twitter_url)
  ```
  Inputs:
  ```bash
  >>>twitter_df.copy().head()

      Tweets	                                            Date
  0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54
  1	@usaucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
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
  ```


##building these package locally
```bash
python setup.py sdist
```

## installing this package from GitHub
```bash
pip install git+https://github.com/JamieJ12/Team-23
```
## updating this package from GitHub
```bash
pip install --upgrade git+https://github.com/JamieJ12/Team-23
```
## license
[MIT](https://choosealicense.com/licenses/mit/)

## Collaborations
### Team LeBron
Precious Sekgathume \n
Jamie Japhta \n
Amukelani Ngobeni \n
Mbuso Biyela \n
Mpumelelo Ndlovu
