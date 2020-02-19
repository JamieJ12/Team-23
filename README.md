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


  ### Function_2

    The Function takes in a list of integers and returns a dictionary

    of the 5 number summary.

    Arguments:

      items (list): List of integers

    The function returns a dictionary with keys: 'max', 'median', 'min',

    'q1', and 'q3', corresponding to the maximum, median, minimum,

    first quartile and

    third quartile, respectively.


      ### Function_3


      The Function inputs a list of date-time strings formatted as:

          'yyyy-mm-dd hh:mm:ss'

          The format : 'yyyy-mm-dd' represents the date and

          The format: 'hh:mm:ss' represents the time

      The function returns a:

      list of strings where each element in the returned list contains

      only the date in the 'yyyy-mm-dd' format.



      ### Function_4
      The function inputs pandas dataframe and

        returns a modified dataframe that includes two new columns

        that contain information about the municipality and hashtag of the tweet.


        Arguments:

        The variable 'df' is the pandas input.

        With added column of extracted hashtags from each tweet

        using 'mun_dict' dictionary and inserts

        the result into a new column named 'municipality' in the same dataframe.


        Function_5

          The function calculates the number of tweets that were posted per day.

          Arguments:

          The index of the new dataframe is 'Date' in the format:

              'yyyy-mm-dd',

          and the column of the new dataframe is 'Tweets',

          corresponding to the date and number of tweets, respectively.

          The function returns the number of tweets per day.



    ### Function_6

            The function splits the sentences in a dataframe's column into

            a list of the separate words.:

            Arguments:

            List is in the column named 'Splits Tweets'

            Function takes in dataframe in the column named 'Tweets'


            Returns a modified dataframe with a new column of a list of individual words


            ### Function_7
              Function removes English stop words from a tweet.


              Arguments:

              Function takes in pandas dataframe

              It tokenisis the sentences according to the definition in function 6


              Returns a modified dataframe with an added column of tweets without stop_words.




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
