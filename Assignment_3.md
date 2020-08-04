# Assignment 3
## NESC 3505


```python
blue = []
orange = []
```

## Flanker Data

We'll be working with data from the same study as we used in Assignment 2. However, in Assignment 2 I gave you a "sanitized" version of the data, where I had done a bit of clean-up to extract just the information I wanted you to work with. In this assignment you'll get experience starting with the raw data and extracting the necessary information yourself. 

The naming convention for this data set was `[subjectID]_[date]_[time]`, with the date represented as YYYY_MM_DD and the time (when the experiment was started) as HH_MM.

Each subject's data file is in a sub-directory with that subject's name and the date they were run. These are listed in the `subjects` list below for you. The sub-directory contains three files, all named with the naming convention above, but with different extensions (remember, extensions are teh bit after teh period in a filename, that indicates what type of file it is).  The three files are:
- `[ID]_code.py` - the python file that ran the experiment - i.e., presented the stimuli and collected responses
- `[ID]_data.txt` - the data file you will want to open
- `[ID]_trigger.txt` - an additional data file not of interest to us

I've included the "extra" files and complicated directory structure because this is what real study data typically looks like. So, it's good experience for you to see this, and learn how to read in just the specific file you need. 


### Subject Listing


```python
subjects = ['spid10_2014_06_17_17_44', 'spid12_2014_06_20_15_11']
```

We're going to import the data as a pandas DataFrame, so your first step is to import pandas with the abbreviation `pd`. Also import NumPy (as `np`) and `matplotlib.pyplot` as `plt`.

<font color=blue ><h4>Q1</h4></font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### Read and examine a data file 

In working with a new data set, the first thing you should do is open up the first data file, and see what it looks like. Does it have a header? If so, what are the column names? Are there any issues like missing data? 

Your first challenge is that the data file you want is in a subdirectory, so you need to tell Python where to find it. I coding-world, the set of directories/sub-directories that a file is in is called it's **path**, and directory names are separated by `/` characters. Since the first subject ID is `spid10_2014_06_17_17_44` and the data file we want is in that, with the name `[ID]_data.txt`, the path to this file is: 
`spid10_2014_06_17_17_44/spid10_2014_06_17_17_44_data.txt`

So, to load in the file you need to create a string like the above. Of course, you could type that in (hard-code it), but that wouldn't be very pythonic, nor would it be useful when you want to read in more subjects' data files. So the better way is to build the string for the path up from variables. Try to do this in the cell below; don't worry about loading the file yet, just create a variable called `in_file` that contains the string above, built from slicing the `subjects` variable (selecting the first entry in the list) and using the `+` operator to combine variables and strings together.

<font color=blue ><h4>Q2</h4></font>

<font color=red> Correct code, but going forward, try to apply the convention of space between code elements (e.g., `subjects[0] + '/' + ...`). It's easier for everyone to read: your teammates, us, and even yourself. </font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
in_file = subjects[0]+'/'+subjects[0]+'_data.txt'

# The print command below will help you confirm you have the string right, 
# before you try to use it to read the data file
print(in_file)
```

    spid10_2014_06_17_17_44/spid10_2014_06_17_17_44_data.txt


Now read spid10's data file into a pandas DataFrame called `df` by using `pd.read_csv()` with the `in_file` variable as the input:

<font color=blue ><h4>Q3</h4></font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df = pd.read_csv(in_file)
```

Look at the head of the DataFrame to see the results:

<font color=blue ><h4>Q4</h4></font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
print(df.head())
```

      id\tyear\tmonth\tday\thour\tminute\tmapping\tmessageViewingTime\tblock\ttrialNum\ttargetLocation\ttarget\tflankers\trt\tresponse\terror\tanticipation\tfeedbackResponse\ttargetOnError
    0  spid10\t2014\t06\t17\t17\t44\t0\t4.395697256\t...                                                                                                                                    
    1  spid10\t2014\t06\t17\t17\t44\t0\t4.395697256\t...                                                                                                                                    
    2  spid10\t2014\t06\t17\t17\t44\t0\t4.395697256\t...                                                                                                                                    
    3  spid10\t2014\t06\t17\t17\t44\t0\t4.395697256\t...                                                                                                                                    
    4  spid10\t2014\t06\t17\t17\t44\t0\t4.395697256\t...                                                                                                                                    


Well, that doesn't look right, does it? We'll need to use some additional arguments to `pd.read_csv()` in order to get it right. 

The issue is that our input file is a text file, with the extension `.txt`. `pd.read_csv()` assumes that the input you give it is a CSV (comma-separated values) file, which uses commas to separate the entries in each row that should be in separate columns. However, our text files use tabs, rather than commas, to separate the columns. We can tell this because in the output above, the first line (column headers) has a bunch of `\t`s in it. The string `\t` is a special code used in unix/linux systems and many programming languages to indicate a tab. The `\` is a special **escape character** that tells Python not to interpret the next character literally as a string, but as a code.

Take a look at [the API for pandas.read_csv()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to get insight on how to tell pandas to use commas as the column separators. You'll see the `sep=` option, along with a note that pandas uses a comma by default. To override this default, we need to use `sep='\t'`. 

<font color=blue ><h4>Q5</h4></font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df=pd.read_csv(in_file, sep='\t')
```

Look at the head of the DataFrame to see the results:

<font color=blue ><h4>Q6</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
print(df.head())
```

           id  year  month  day  hour  minute  mapping  messageViewingTime  \
    0  spid10  2014      6   17    17      44        0            4.395697   
    1  spid10  2014      6   17    17      44        0            4.395697   
    2  spid10  2014      6   17    17      44        0            4.395697   
    3  spid10  2014      6   17    17      44        0            4.395697   
    4  spid10  2014      6   17    17      44        0            4.395697   
    
          block  trialNum targetLocation target     flankers        rt response  \
    0  practice         1          right  white    congruent  0.723172    white   
    1  practice         1          right  white    congruent  0.723172    white   
    2  practice         1          right  white    congruent  0.723172    white   
    3  practice         2          right  white  incongruent       NaN      NaN   
    4  practice         2          right  white  incongruent       NaN      NaN   
    
       error  anticipation  feedbackResponse  targetOnError  
    0  False         False             False       0.069474  
    1  False         False             False       0.069474  
    2  False         False             False       0.069474  
    3    NaN         False              True       0.066798  
    4    NaN         False              True       0.066798  


OK, that should look much better! 

(Side note: there are a lot more columns in this data file than the version I gave you last time. Again, this is because before you got the "sanitized" version whereas now you get the "raw" version. We'll work with some of these extra columns in this assignment, and others will just be ignored. It's not uncommon to have columns (variables) in a data set that are not of interest for a specific analysis you're running.)

There are two more issues with this data file that are evident from looking at the first few lines. One is that it has missing values (`NaN`) in the `rt` column. The other is that every data row seems to be repeated 3 times. You can confirm this by looking at a longer `head` of the data (say, 24 lines):

<font color=blue ><h4>Q7</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
print(df.head(24))
```

            id  year  month  day  hour  minute  mapping  messageViewingTime  \
    0   spid10  2014      6   17    17      44        0            4.395697   
    1   spid10  2014      6   17    17      44        0            4.395697   
    2   spid10  2014      6   17    17      44        0            4.395697   
    3   spid10  2014      6   17    17      44        0            4.395697   
    4   spid10  2014      6   17    17      44        0            4.395697   
    5   spid10  2014      6   17    17      44        0            4.395697   
    6   spid10  2014      6   17    17      44        0            4.395697   
    7   spid10  2014      6   17    17      44        0            4.395697   
    8   spid10  2014      6   17    17      44        0            4.395697   
    9   spid10  2014      6   17    17      44        0            4.395697   
    10  spid10  2014      6   17    17      44        0            4.395697   
    11  spid10  2014      6   17    17      44        0            4.395697   
    12  spid10  2014      6   17    17      44        0            4.395697   
    13  spid10  2014      6   17    17      44        0            4.395697   
    14  spid10  2014      6   17    17      44        0            4.395697   
    15  spid10  2014      6   17    17      44        0            4.395697   
    16  spid10  2014      6   17    17      44        0            4.395697   
    17  spid10  2014      6   17    17      44        0            4.395697   
    18  spid10  2014      6   17    17      44        0            4.395697   
    19  spid10  2014      6   17    17      44        0            4.395697   
    20  spid10  2014      6   17    17      44        0            4.395697   
    21  spid10  2014      6   17    17      44        0            4.395697   
    22  spid10  2014      6   17    17      44        0            4.395697   
    23  spid10  2014      6   17    17      44        0            4.395697   
    
           block  trialNum targetLocation target     flankers        rt response  \
    0   practice         1          right  white    congruent  0.723172    white   
    1   practice         1          right  white    congruent  0.723172    white   
    2   practice         1          right  white    congruent  0.723172    white   
    3   practice         2          right  white  incongruent       NaN      NaN   
    4   practice         2          right  white  incongruent       NaN      NaN   
    5   practice         2          right  white  incongruent       NaN      NaN   
    6   practice         3           left  black    congruent  0.342453    black   
    7   practice         3           left  black    congruent  0.342453    black   
    8   practice         3           left  black    congruent  0.342453    black   
    9   practice         4          right  white  incongruent  0.311569    white   
    10  practice         4          right  white  incongruent  0.311569    white   
    11  practice         4          right  white  incongruent  0.311569    white   
    12  practice         5           left  white    congruent  0.328021    black   
    13  practice         5           left  white    congruent  0.328021    black   
    14  practice         5           left  white    congruent  0.328021    black   
    15  practice         6          right  black    congruent  0.353063    black   
    16  practice         6          right  black    congruent  0.353063    black   
    17  practice         6          right  black    congruent  0.353063    black   
    18  practice         7           left  black    congruent  0.335421    black   
    19  practice         7           left  black    congruent  0.335421    black   
    20  practice         7           left  black    congruent  0.335421    black   
    21  practice         8          right  black  incongruent  0.411666    black   
    22  practice         8          right  black  incongruent  0.411666    black   
    23  practice         8          right  black  incongruent  0.411666    black   
    
        error  anticipation  feedbackResponse  targetOnError  
    0   False         False             False       0.069474  
    1   False         False             False       0.069474  
    2   False         False             False       0.069474  
    3     NaN         False              True       0.066798  
    4     NaN         False              True       0.066798  
    5     NaN         False              True       0.066798  
    6   False         False             False       0.071909  
    7   False         False             False       0.071909  
    8   False         False             False       0.071909  
    9   False         False             False       0.069050  
    10  False         False             False       0.069050  
    11  False         False             False       0.069050  
    12   True         False             False       0.067132  
    13   True         False             False       0.067132  
    14   True         False             False       0.067132  
    15  False         False             False       0.068103  
    16  False         False             False       0.068103  
    17  False         False             False       0.068103  
    18  False         False             False       0.070834  
    19  False         False             False       0.070834  
    20  False         False             False       0.070834  
    21  False         False             False       0.071013  
    22  False         False             False       0.071013  
    23  False         False             False       0.071013  


So it does look like the "triplication" is a consistent issue. However, it's good to be thorough, so why don't you check the last 24 lines of the data file (the "tail") as well?

<font color=blue ><h4>Q8</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
print(df.tail(24))
```

             id  year  month  day  hour  minute  mapping  messageViewingTime  \
    840  spid10  2014      6   17    17      44        0           74.063199   
    841  spid10  2014      6   17    17      44        0           74.063199   
    842  spid10  2014      6   17    17      44        0           74.063199   
    843  spid10  2014      6   17    17      44        0           74.063199   
    844  spid10  2014      6   17    17      44        0           74.063199   
    845  spid10  2014      6   17    17      44        0           74.063199   
    846  spid10  2014      6   17    17      44        0           74.063199   
    847  spid10  2014      6   17    17      44        0           74.063199   
    848  spid10  2014      6   17    17      44        0           74.063199   
    849  spid10  2014      6   17    17      44        0           74.063199   
    850  spid10  2014      6   17    17      44        0           74.063199   
    851  spid10  2014      6   17    17      44        0           74.063199   
    852  spid10  2014      6   17    17      44        0           74.063199   
    853  spid10  2014      6   17    17      44        0           74.063199   
    854  spid10  2014      6   17    17      44        0           74.063199   
    855  spid10  2014      6   17    17      44        0           74.063199   
    856  spid10  2014      6   17    17      44        0           74.063199   
    857  spid10  2014      6   17    17      44        0           74.063199   
    858  spid10  2014      6   17    17      44        0           74.063199   
    859  spid10  2014      6   17    17      44        0           74.063199   
    860  spid10  2014      6   17    17      44        0           74.063199   
    861  spid10  2014      6   17    17      44        0           74.063199   
    862  spid10  2014      6   17    17      44        0           74.063199   
    863  spid10  2014      6   17    17      44        0           74.063199   
    
        block  trialNum targetLocation target     flankers        rt response  \
    840     5        41          right  black    congruent  0.479286    black   
    841     5        41          right  black    congruent  0.479286    black   
    842     5        41          right  black    congruent  0.479286    black   
    843     5        42           left  white    congruent  0.499685    white   
    844     5        42           left  white    congruent  0.499685    white   
    845     5        42           left  white    congruent  0.499685    white   
    846     5        43          right  white    congruent  0.485177    white   
    847     5        43          right  white    congruent  0.485177    white   
    848     5        43          right  white    congruent  0.485177    white   
    849     5        44           left  black    congruent  0.424173    white   
    850     5        44           left  black    congruent  0.424173    white   
    851     5        44           left  black    congruent  0.424173    white   
    852     5        45          right  black  incongruent  0.446264    white   
    853     5        45          right  black  incongruent  0.446264    white   
    854     5        45          right  black  incongruent  0.446264    white   
    855     5        46          right  white  incongruent  0.539675    white   
    856     5        46          right  white  incongruent  0.539675    white   
    857     5        46          right  white  incongruent  0.539675    white   
    858     5        47           left  black    congruent  0.330191    black   
    859     5        47           left  black    congruent  0.330191    black   
    860     5        47           left  black    congruent  0.330191    black   
    861     5        48           left  black    congruent  0.430980    black   
    862     5        48           left  black    congruent  0.430980    black   
    863     5        48           left  black    congruent  0.430980    black   
    
         error  anticipation  feedbackResponse  targetOnError  
    840  False         False             False       0.069021  
    841  False         False             False       0.069021  
    842  False         False             False       0.069021  
    843  False         False             False       0.068479  
    844  False         False             False       0.068479  
    845  False         False             False       0.068479  
    846  False         False             False       0.068470  
    847  False         False             False       0.068470  
    848  False         False             False       0.068470  
    849   True         False              True       0.064946  
    850   True         False              True       0.064946  
    851   True         False              True       0.064946  
    852   True         False             False       0.068929  
    853   True         False             False       0.068929  
    854   True         False             False       0.068929  
    855  False         False             False       0.069080  
    856  False         False             False       0.069080  
    857  False         False             False       0.069080  
    858  False         False             False       0.068443  
    859  False         False             False       0.068443  
    860  False         False             False       0.068443  
    861  False         False             False       0.068893  
    862  False         False             False       0.068893  
    863  False         False             False       0.068893  


### Missing Values?

Since the first lines of a data file obviously don't represent its entirety, it would be good to get a summary of how many missing values there are in the data set. You can do this with `pd.isna()` (or the equivalent `pd.isnull()`), which will output `True` or `False` for every cell of the DataFrame. That alone is not any more useful than looking at the original data, however you can *chain* that command with the `.sum()` method to get the total number of `True` values in each column (remember that in Python, `true` = `1` and `False` = `0`). 

Do this below: run `isna()` on `df` and chain it with the `.sum()` method.

<font color=blue ><h4>Q9</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.isnull().sum()
```




    id                    0
    year                  0
    month                 0
    day                   0
    hour                  0
    minute                0
    mapping               0
    messageViewingTime    0
    block                 0
    trialNum              0
    targetLocation        0
    target                0
    flankers              0
    rt                    3
    response              3
    error                 3
    anticipation          0
    feedbackResponse      0
    targetOnError         0
    dtype: int64



I'll note, for the record, that if this were your own data you should look more extensively at the entire data file, and other data files, to confirm that this "triplication" of the rows was a consistent issue. For this assignment, you can trust me that it is consistent across all data sets. Why, you ask? I don't honestly know. Although this data came from a study run in my lab, it was programmed by one former student and run by another. Neither of them are around any more to ask, nor would they likely remember since it was run years ago. This is quite common in research labs, especially where studies are run by students who are, by definition, still learning best practices. I tell you this for two reasons. Firstly, to encourage you to pay close attention if and when you're designing and running your own experiments, to try to avoid issues of weird data files, and/or document them. Secondly, to prepare you that this is the nature of real data. Very often, as much or more time is spent "cleaning" the data as actually analyzing it! That's part off being a data scientist.

### Data Cleaning

The next things we need to do are:
- decide how to deal with the `NaN`s
- remove the redundant lines

In terms of the missing data, it turns out these are just trials on which the participant didn't make a button press response. We have (at least) three options:
1. Leave these as-is. 
2. Remove all rows with missing data
3. Replace (impute) the missing values with actual values. 

Option 3 was covered in the DataCamp lessons. Imputation of missing data is sometimes done in psychology and neuroscience studies, especially if we have lots of variables, and only one data point per subject (e.g., a score on a standardized test completed by each subject). Usually the reason for imputing data is that statistical methods such as ANOVAs do not allow for missing data, so without imputation we might have to discard a subject's data, even if they are only missing data from one test among many that were administered. 

However, in the current case, it doesn't make sense to "make up" a reaction time on a trial when a participant didn't make a response at all. So we could remove those trials entirely. On the other hand, we might want to report how many trials, on average, our participants failed to respond to, or we might want to treat those the same as errors. 

Although missing data is problematic for things like ANOVAs, it is not an issue for EDA summary statistics in pandas. Indeed, [pandas' documentation explicitly states](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#calculations-with-missing-data) that missing data is ignored in computing values such as the mean and standard deviation.  

So, we could probably safely keep the NaNs in the data. On the other hand, you learned in *Manipulating DataFrames with pandas* how to use the `.dropna()` method. And as they say, "when you have a hammer, everything looks like a nail". So let's drop the any rows containing any NaN values:

<font color=blue ><h4>Q10</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df = df.dropna()
```

Confirm that this was successful by re-running the command from above that counted the total number of missing values:

<font color=blue ><h4>Q11</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.isna().sum()
```




    id                    0
    year                  0
    month                 0
    day                   0
    hour                  0
    minute                0
    mapping               0
    messageViewingTime    0
    block                 0
    trialNum              0
    targetLocation        0
    target                0
    flankers              0
    rt                    0
    response              0
    error                 0
    anticipation          0
    feedbackResponse      0
    targetOnError         0
    dtype: int64



### Remove repeated rows

So after that long-winded (but important!) discussion, all we need to do is figure out how to remove every third row of this pandas DataFrame. This is super-easy just using slicing. Go for it! 


**Note:** Of course by "easy" I don't mean it will be necessarily be easy to figure out. But the end result is a very short snippet of code. In working on this, first play around with slicing the `df` DataFrame without assigning the result to a variable, e.g., a line like:
`df.iloc[0,:]`

This will show you the output immediately, so you can tell if you got it right or not. Once you've figured it out, assign the new DataFrame (the output of your slicing command) to `df`. **This will overwrite the original `df` DataFrame, so make sure you have the code right before you run it**. 

Worst case, if you do mess up `df`, just restart your kernel and run the cells above to get the original `df` back.



```python

```


```python
# Use this cell to figure it out before assigning the result to df
df.iloc[0::3,:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>mapping</th>
      <th>messageViewingTime</th>
      <th>block</th>
      <th>trialNum</th>
      <th>targetLocation</th>
      <th>target</th>
      <th>flankers</th>
      <th>rt</th>
      <th>response</th>
      <th>error</th>
      <th>anticipation</th>
      <th>feedbackResponse</th>
      <th>targetOnError</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>1</td>
      <td>right</td>
      <td>white</td>
      <td>congruent</td>
      <td>0.723172</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.069474</td>
    </tr>
    <tr>
      <th>6</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>3</td>
      <td>left</td>
      <td>black</td>
      <td>congruent</td>
      <td>0.342453</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.071909</td>
    </tr>
    <tr>
      <th>9</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>4</td>
      <td>right</td>
      <td>white</td>
      <td>incongruent</td>
      <td>0.311569</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.069050</td>
    </tr>
    <tr>
      <th>12</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>5</td>
      <td>left</td>
      <td>white</td>
      <td>congruent</td>
      <td>0.328021</td>
      <td>black</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.067132</td>
    </tr>
    <tr>
      <th>15</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>6</td>
      <td>right</td>
      <td>black</td>
      <td>congruent</td>
      <td>0.353063</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068103</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>849</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>44</td>
      <td>left</td>
      <td>black</td>
      <td>congruent</td>
      <td>0.424173</td>
      <td>white</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>0.064946</td>
    </tr>
    <tr>
      <th>852</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>45</td>
      <td>right</td>
      <td>black</td>
      <td>incongruent</td>
      <td>0.446264</td>
      <td>white</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.068929</td>
    </tr>
    <tr>
      <th>855</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>46</td>
      <td>right</td>
      <td>white</td>
      <td>incongruent</td>
      <td>0.539675</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.069080</td>
    </tr>
    <tr>
      <th>858</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>47</td>
      <td>left</td>
      <td>black</td>
      <td>congruent</td>
      <td>0.330191</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068443</td>
    </tr>
    <tr>
      <th>861</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>48</td>
      <td>left</td>
      <td>black</td>
      <td>congruent</td>
      <td>0.430980</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068893</td>
    </tr>
  </tbody>
</table>
<p>287 rows × 19 columns</p>
</div>



<font color=blue ><h4>Q12</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
# use this cell to assign the result to df once you have the right output
df = df.iloc[::3,:]
```

Run the cell below to confirm you have only one row per trial (so the `trialNum` column should read 1, 2, 3, 4, etc.)

<font color=blue ><h4>Q13</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>mapping</th>
      <th>messageViewingTime</th>
      <th>block</th>
      <th>trialNum</th>
      <th>targetLocation</th>
      <th>target</th>
      <th>flankers</th>
      <th>rt</th>
      <th>response</th>
      <th>error</th>
      <th>anticipation</th>
      <th>feedbackResponse</th>
      <th>targetOnError</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>1</td>
      <td>right</td>
      <td>white</td>
      <td>congruent</td>
      <td>0.723172</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.069474</td>
    </tr>
    <tr>
      <th>6</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>3</td>
      <td>left</td>
      <td>black</td>
      <td>congruent</td>
      <td>0.342453</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.071909</td>
    </tr>
    <tr>
      <th>9</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>4</td>
      <td>right</td>
      <td>white</td>
      <td>incongruent</td>
      <td>0.311569</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.069050</td>
    </tr>
    <tr>
      <th>12</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>5</td>
      <td>left</td>
      <td>white</td>
      <td>congruent</td>
      <td>0.328021</td>
      <td>black</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.067132</td>
    </tr>
    <tr>
      <th>15</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>4.395697</td>
      <td>practice</td>
      <td>6</td>
      <td>right</td>
      <td>black</td>
      <td>congruent</td>
      <td>0.353063</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068103</td>
    </tr>
  </tbody>
</table>
</div>



### Remove practice trials

You'll note that in the first rows of the DataFrame (e.g., when you view the head), the `block` column reads 'practice'. Those are, indeed, practice trials. You can use the pandas `unique()` method to see what the other possible values of `block` are in this dataset. Do that in the cell below:

<font color=blue ><h4>Q14</h4>
</font>

<font color=red> Neat. You used unique as a function rather than a method. Works either way. </font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
pd.unique(df['block'])
```




    array(['practice', '1', '2', '3', '4', '5'], dtype=object)



The  point of practice is to give participants a chance to figure out the experiment (which is a bit complicated in this case), and make some errors, ask questions, etc., *before* running the experiment where we hope their data will be a valid reflection of their performance. So we should discard all the practice trials prior to doing EDA. 

The simplest way to remove all the rows from the practice block is actually to simply keep all the values that *don't* have the value of 'practice' in the `block` column. Fill in the Python "not equals" operator in the command below to do this. 

<font color=blue ><h4>Q15</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df = df[df['block'] != 'practice']
```

Run a command that confirms that there are no practice trials left in `df`

<font color=blue ><h4>Q16</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
print(df)
```

             id  year  month  day  hour  minute  mapping  messageViewingTime  \
    144  spid10  2014      6   17    17      44        0           13.251555   
    147  spid10  2014      6   17    17      44        0           13.251555   
    150  spid10  2014      6   17    17      44        0           13.251555   
    153  spid10  2014      6   17    17      44        0           13.251555   
    156  spid10  2014      6   17    17      44        0           13.251555   
    ..      ...   ...    ...  ...   ...     ...      ...                 ...   
    849  spid10  2014      6   17    17      44        0           74.063199   
    852  spid10  2014      6   17    17      44        0           74.063199   
    855  spid10  2014      6   17    17      44        0           74.063199   
    858  spid10  2014      6   17    17      44        0           74.063199   
    861  spid10  2014      6   17    17      44        0           74.063199   
    
        block  trialNum targetLocation target     flankers        rt response  \
    144     1         1           left  white  incongruent  0.551714    white   
    147     1         2          right  black    congruent  0.344355    black   
    150     1         3           left  black  incongruent  0.282131    white   
    153     1         4           left  black    congruent  0.388339    black   
    156     1         5           left  black  incongruent  0.741977    black   
    ..    ...       ...            ...    ...          ...       ...      ...   
    849     5        44           left  black    congruent  0.424173    white   
    852     5        45          right  black  incongruent  0.446264    white   
    855     5        46          right  white  incongruent  0.539675    white   
    858     5        47           left  black    congruent  0.330191    black   
    861     5        48           left  black    congruent  0.430980    black   
    
         error  anticipation  feedbackResponse  targetOnError  
    144  False         False             False       0.068436  
    147  False         False             False       0.068915  
    150   True         False             False       0.066689  
    153  False         False             False       0.068476  
    156  False         False             False       0.069494  
    ..     ...           ...               ...            ...  
    849   True         False              True       0.064946  
    852   True         False             False       0.068929  
    855  False         False             False       0.069080  
    858  False         False             False       0.068443  
    861  False         False             False       0.068893  
    
    [240 rows x 19 columns]


### Reaction Times

First off, convert the `rt` column to milliseconds

<font color=blue ><h4>Q17</h4>
</font>

<font color=red> Converting seconds into milliseconds requires multiplication, not division. </font>

<font color=blue> 0/1 </font>


```python
blue = blue + [0.]
```


```python
df['rt'] = df['rt']/1000
```

#### Examining the RT distribution

In most behavioural studies, RTs are not normally distributed. Recall that a normal distribution has a mean and a standard deviation, and no *skew*. That is to say, there are typically an equal number and distribution of values above and below the mean. RTs tend to be skewed, because there are fundamental limits on how fast a human can process information and make a motor response, which sets a lower limit on RTs. However, the upper limit (slow RTs) has much more range. In some experiments, participants can wait as long as they want to make a response. In other experiments, there is a limited response window, but still there tends to be a wider tail on the right side of the distribution, when you plot it. 

Let's see if our RT data is skewed. First, use the pandas method `.describe()` to display descriptive stats for the RT data:

<font color=blue ><h4>Q18</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>mapping</th>
      <th>messageViewingTime</th>
      <th>trialNum</th>
      <th>rt</th>
      <th>targetOnError</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>240.0</td>
      <td>240.0</td>
      <td>240.0</td>
      <td>240.0</td>
      <td>240.0</td>
      <td>240.0</td>
      <td>240.000000</td>
      <td>240.000000</td>
      <td>240.000000</td>
      <td>240.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2014.0</td>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>44.0</td>
      <td>0.0</td>
      <td>98.148119</td>
      <td>24.500000</td>
      <td>0.000428</td>
      <td>0.068645</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>111.517759</td>
      <td>13.882351</td>
      <td>0.000095</td>
      <td>0.001886</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2014.0</td>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>44.0</td>
      <td>0.0</td>
      <td>2.799539</td>
      <td>1.000000</td>
      <td>0.000270</td>
      <td>0.063109</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2014.0</td>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>44.0</td>
      <td>0.0</td>
      <td>13.251555</td>
      <td>12.750000</td>
      <td>0.000358</td>
      <td>0.068356</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2014.0</td>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>44.0</td>
      <td>0.0</td>
      <td>74.063199</td>
      <td>24.500000</td>
      <td>0.000410</td>
      <td>0.068564</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2014.0</td>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>44.0</td>
      <td>0.0</td>
      <td>90.386549</td>
      <td>36.250000</td>
      <td>0.000479</td>
      <td>0.069160</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2014.0</td>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>44.0</td>
      <td>0.0</td>
      <td>310.239753</td>
      <td>48.000000</td>
      <td>0.000864</td>
      <td>0.076214</td>
    </tr>
  </tbody>
</table>
</div>



Next plot a histogram of RTs:

<font color=blue ><h4>Q19</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
# put your plotting code here

plt.hist(df['rt'])
# Don't modify the code below here
# Add a solid line at the median and dashed lines at the 25th and 75th 
# percentiles (done for you)
plt.axvline(df['rt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['rt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['rt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()
```




![png](Assignment_3_files/Assignment_3_82_0.png)



Does the histogram look normally distributed, or skewed? Explain.

<font color=blue ><h4>Q20</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```

The data does not look normally distributed - It looks right skewed 

Plot the normed cumulative density function (CDF) of the RTs:

<font color=blue ><h4>Q21</h4>
</font>

<font color=red> Don't forget the keyword argument for the "D" in "CDF".</font>

<font color=blue> 0.5/1 </font>


```python
blue = blue + [0.5]
```


```python
# put your plotting code here
plt.hist(df['rt'], cumulative = True)
# Don't modify the code below here
# Add a solid line at the median and dashed lines at the 25th and 75th 
# percentiles (done for you)
plt.axvline(df['rt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['rt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['rt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

plt.show()
```




![png](Assignment_3_files/Assignment_3_90_0.png)



How can you tell from the CDF whether or not the data are skewed? 

<font color=blue ><h4>Q22</h4>
</font>

<font color=red> How so? </font>

<font color=blue> 0/1 </font>


```python
blue = blue + [0.]
```

Yes the CDF confirms that the data is negatively skewed 

### RT transformations

While the skew in the RT data makes sense, for the reasons described above, it's problematic when running statistics on the data. This is because many conventional statistical tests, like *t*-tests and ANOVAs, assume that the data are normally distributed. Using skewed data can cause unreliable results. 

For this reason, many researchers apply some transformation to RTs to make their distribution more normal (statistically normal, that is). A common one is to take the logarithm of the RT values: $log(RT)$; another is to take the inverse: $1/RT$. 


The code below will add a column to your DataFrame called `logrt`. Add a line to plot the histogram of the log-transformed data:

<font color=blue ><h4>Q23</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
# log-transform the rt data (done for you)
df['logrt'] = np.log(df['rt'])

# put your plotting code here

plt.hist(df['logrt'])
# Don't modify the code below here
# Add a solid line at the median and dashed lines at the 25th and 75th 
# percentiles (done for you)
plt.axvline(df['logrt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['logrt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['logrt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()
```




![png](Assignment_3_files/Assignment_3_99_0.png)



Likewise, the code below will create an `invrt` column containing the inverse transform of RT. Plot its histogram as well:

<font color=blue ><h4>Q24</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
# compute the inverse of rt (done for you)
df['invrt'] = 1/df['rt']

# put your plotting code here
plt.hist(df['invrt'])

# Don't modify the code below here
# Add a solid line at the median and dashed lines at the 25th and 75th 
# percentiles (done for you)
plt.axvline(df['invrt'].describe()['25%'], 0, 1, color='turquoise', linestyle='--')
plt.axvline(df['invrt'].median(), 0, 1, color='cyan', linestyle='-')
plt.axvline(df['invrt'].describe()['75%'], 0, 1, color='turquoise', linestyle='--')

# Rememebr to use plt.show() to see your plots (often they show anyway, but with some garbagy text at the top)
plt.show()
```




![png](Assignment_3_files/Assignment_3_103_0.png)



Does one of these two transforms produce a more normal-looking distribution? If so, which one? 

<font color=blue ><h4>Q25</h4></font>

<font color=red> While the log transformation looks more like a bell curve shape, there's still the skew. Although the inverse doesn't have a lovely bell shape, its frequency distribution is more symmetrical. </font>

<font color=blue> 0/1 </font>


```python
blue = blue + [0.]
```

Yes the histogram using the log-transformed rt data is a much more normal-looking distribution

### Grouping by experimental condition

Recall that these data are from a "flanker" experiment in which participants had to respond with a left or right button press, depending on whether the target (centre) arrow pointed left or right. The target arrow was flanked with two arrows on either side that were either congruent (pointed in same direction) or incongruent (opposite direction). 

Our focus in exploring the data will be on errors and reaction times (RTs).

Let's start by finding out how many trials we have in each condition. Use the `groupby()` method, chained with the `.cout()` method, to group the DataFrame by `flankers` and count the number of data points (rows) in each flanker condition.

<font color=blue ><h4>Q26</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.groupby('flankers').count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>mapping</th>
      <th>messageViewingTime</th>
      <th>block</th>
      <th>trialNum</th>
      <th>targetLocation</th>
      <th>target</th>
      <th>rt</th>
      <th>response</th>
      <th>error</th>
      <th>anticipation</th>
      <th>feedbackResponse</th>
      <th>targetOnError</th>
      <th>logrt</th>
      <th>invrt</th>
    </tr>
    <tr>
      <th>flankers</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>congruent</th>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
    </tr>
    <tr>
      <th>incongruent</th>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
    </tr>
  </tbody>
</table>
</div>



You should get a DataFrame with two rows (congruent and incongruent), and a count in each of the columns of the original DataFrame. A good start, but a bit TMI and less focused on what we might actually want to know (about errors and RTs).

So, following the examples in Chapter 4 of *Manipulating DataFrames with pandas*, use the "split-apply-combine" approach to show the counts only for `rt` and `error`. 

<font color=blue ><h4>Q27</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.groupby('flankers')[['rt','error']].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rt</th>
      <th>error</th>
    </tr>
    <tr>
      <th>flankers</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>congruent</th>
      <td>120</td>
      <td>120</td>
    </tr>
    <tr>
      <th>incongruent</th>
      <td>120</td>
      <td>120</td>
    </tr>
  </tbody>
</table>
</div>



Although this was a balanced experiment (i.e., equal number of trials in each condition), the numbers above are not equal. Thinking back to discussion earlier in this assignment, why do you think that is? 

<font color=blue ><h4>Q28</h4>
</font>

<font color=blue> Removed </font>

The numbers are equal?

### About this experiment
#### (A side note, but an important one)

The experiment that generated the data was actually more complicated than I've explained previously. In fact, I told a small lie. Although this WAS a flanker study, the stimuli were not arrows. Instead, they were actually circles — the targets were circles that were either black or white, and the flankers were a set of circles surrounding the target, that were also either black or white. So "congruent" in this case means the targets were the same colour as the flankers, and "incongruent" means the target and flankers were opposite colours. 

This experiment combined the flanker task with a second task, known as the *Simon task*. The "Simon effect" describes a phenomenon in which people's responses are faster if they are made by the hand on the same side of the screen as the stimulus they are responding to. So for example, if you are holding a game controller and are told to press the left trigger button when you see a white stimulus, and the right trigger button when you see a black stimulus, you should respond (on average) faster when white stimuli are shown on the left side of the screen, and when black stimuli are shown on the right side of the screen — since the side of the screen is congruent with the mapping between colour and response button. 

This study combined the flanker and Simon tasks by having participants fixate their eyes on a stimulus in the centre of the screen, and then presenting the target and flanker stimuli on either the left or the right side of the screen. Since the targets could be either white or black, and the participants had to press the right button for one colour, and the left button for the other, we can explore both the flanker and Simon effects in one study, as well as seeing how they interact. 

Why would we do this, you ask? While it simply seems like the special brad of torture that cognitive psychologists enjoy inflicting on undergraduate students, there was a deeper reason. Both the flanker and Simon tasks purport to tap what is called *executive function* — specifically, the ability to inhibit a "prepotent" (dominant, intuitive, impulsive) response in order to produce a correct response. In the flanker task, you have to filter out (inhibit) the relatively greater number of flanking stimuli and focus on responding to the one in the centre; in the Simon task, you have to inhibit your tendency to press the button that's on the same side of the screen as the stimulus. Both tasks are relatively easy if you're given lots of time, but in experiments we present the stimuli for very short durations to make it hard (insert evil laughter here). 

Conceptually, both the flanker and Simon tasks seem to tap into this construct of "executive function", but it's not known if they are tapping the same process or two different ones. So by combining the two tasks, we can tell if the "double whammy" of presenting a stimulus with incongruent flankers AND on the side incongruent with the response hand causes people more trouble than either of those alone. 

Our hypotheses for RT are below. Similarly, for error rate we expected the least errors in the double-congruent condition, and the most in the double-incongruent condition.

| Response hand | Flankers | |
| --- | --- |--- |
| | **Congruent** | **Incongruent** |
| **Congruent** | Fastest | Slow |
| **Incongruent** | Slow | Slowest |


### Exploring more variables

So now you have some insight into the meaning of some of the other columns in this DataFrame. **Target** is the colour of the target, and **targetLocation** tells us whether the target was on the left or right side of the screen. As well, there's a column called **mapping** which indicates the "mapping" between colours and left/right button presses. The mappings are as follows: 

| mapping | left button  | right button | 
| ------- | ----- | ----- |
| 0       | white | black |
| 1       | black | white |

In a rare bit of sympathy towards our participants, we didn't change the mapping during the study for any individual, so mapping is a between-subjects variable; that is, different subjects got mapping 0 or 1, but mapping is consistent across the entire DataFrame for each individual.

With this in mind, we can break down our table counting trials even further. Repeat the the "split-apply-combine"  command you used above to show the counts for rt and error, but broken down by both `flankers` and `target`.

<font color=blue ><h4>Q29</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.groupby(['flankers','target'])[['rt','error']].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>rt</th>
      <th>error</th>
    </tr>
    <tr>
      <th>flankers</th>
      <th>target</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">congruent</th>
      <th>black</th>
      <td>60</td>
      <td>60</td>
    </tr>
    <tr>
      <th>white</th>
      <td>60</td>
      <td>60</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">incongruent</th>
      <th>black</th>
      <td>60</td>
      <td>60</td>
    </tr>
    <tr>
      <th>white</th>
      <td>60</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>



### Derive and encode Simon condition

While your table above now breaks things down in a more fine-grained way, it doesn't actually align with the experimental design. One confusing thing about the way these data are stored is that, while we have one column clearly indicating whether our flankers were congruent or not (the intuitively-named `flankers` column), there is no column that uniquely and clearly tells us whether each trial was congruent or not for the Simon task component. This is encoded across three columns — `target`, `targetLocation`, and `mapping`. That is, once we know the mapping between response hand and colour, AND which side the stimulus was presented on, we will know whether a value of "black" in the `target` column is Simon-congruent or Simon-incongruent. 

This is, obviously, not something we want to constantly be trying to compute in our heads when looking at the data frame. Nor does it lend itself easily to making a summary table like you just did for the `flanker` column. Instead, you need to flex those Python muscles and create a new column in the DataFrame, called `simon`, which encodes whether each trial was Simon-congruent or Simon-incongruent (note I'm explicitly saying "Simon-congruent or Simon-incongruent" here to try to avoid confusion with flanker-congruent and flanker-incongruent). 

This is more advanced than what has been covered in your lessons so far, but it's a common and useful thing to know. So, I've provided most of the code for you, but left bits for you to fill in, which will hopefully help you to understand what you're doing. 

We use [`np.select`](https://numpy.org/doc/stable/reference/generated/numpy.select.html?highlight=select#numpy.select) to do this; I suggest you click the link to read the API to help you understand what's going on. 

| mapping | left button  | right button | 
| ------- | ----- | ----- |
| 0       | white | black |
| 1       | black | white |

Below, fill in the missing bits after the `==` symbols on all the lines where information is missing. I've done the first three lines for you. Note as well how I'm systematically changing the three variables (`mapping`, `target`, and `targetLocation`) — the rightmost one (`targetLocation`) changes fastest, as we go down the list (`left`-`right`-`left` etc), the middle one changes next most quickly (`black`-`black`-`white` etc) and the leftmost one changes slowest. It's always good to follow systematic patterns like this — it makes for more intuitive, readable code, and also means you're less likely to make errors or forget to include a condition.

<font color=blue ><h4>Q30</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
# first we create a set of conditions — in our cases, the different possible mappings
conditions = [
    (df['mapping'] == 0) & (df['target'] == 'black') & (df['targetLocation'] == 'left'),
    (df['mapping'] == 0) & (df['target'] == 'black') & (df['targetLocation'] == 'right'),
    (df['mapping'] == 0) & (df['target'] == 'white') & (df['targetLocation'] == 'left'),
    (df['mapping'] == 0) & (df['target'] == 'white') & (df['targetLocation'] == 'right'),
    (df['mapping'] == 1) & (df['target'] == 'black') & (df['targetLocation'] == 'left'),
    (df['mapping'] == 1) & (df['target'] == 'black') & (df['targetLocation'] == 'right'),
    (df['mapping'] == 1) & (df['target'] == 'white') & (df['targetLocation'] == 'left'),
    (df['mapping'] == 1) & (df['target'] == 'white') & (df['targetLocation'] == 'right')
    ]

# The mappings below align with the order of the entries in the conditions list above
mapping = ['incongruent', 
           'congruent', 
           'congruent', 
           'incongruent', 
           'congruent', 
           'incongruent', 
           'incongruent', 
           'congruent'
          ]

# This line creates a new column called "simon" based on the conditions and mapping lists above
df['simon'] = np.select(conditions, mapping, default='none')
```

#### Side note

Getting the code above to work took me a frustrating amount of time. Half an hour or more I think (with a break). I found sample code that seemed to do what I wanted, but I kept getting errors. It turned out that the issue was that whereas the correct format for each line of the `conditions` list is:

`(df['mapping']==0) & (df['target'] == 'black') & (df['targetLocation'] == 'left')`

...with each conditional in parentheses, I had instead put the entire set of three conditionals in parentheses:

`(df['mapping']==0 & df['target'] == 'black' & df['targetLocation'] == 'left')`

I say this just so you know, it's not just you who struggles with little details like where the parentheses go!

I'm thinking of writing a book called *Teaching Python the Hard Way*... 


---

Anyway, go ahead and view the head of the DataFrame again to confirm that the `simon` column was created and looks the way you expect. New columns get added to the right side of a DataFrame, so you'll likely need to scroll sideways to see it.

<font color=blue ><h4>Q31</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>mapping</th>
      <th>messageViewingTime</th>
      <th>block</th>
      <th>trialNum</th>
      <th>...</th>
      <th>flankers</th>
      <th>rt</th>
      <th>response</th>
      <th>error</th>
      <th>anticipation</th>
      <th>feedbackResponse</th>
      <th>targetOnError</th>
      <th>logrt</th>
      <th>invrt</th>
      <th>simon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>144</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>incongruent</td>
      <td>0.000552</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068436</td>
      <td>-7.502481</td>
      <td>1812.533282</td>
      <td>congruent</td>
    </tr>
    <tr>
      <th>147</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>congruent</td>
      <td>0.000344</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068915</td>
      <td>-7.973836</td>
      <td>2903.976759</td>
      <td>congruent</td>
    </tr>
    <tr>
      <th>150</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>3</td>
      <td>...</td>
      <td>incongruent</td>
      <td>0.000282</td>
      <td>white</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.066689</td>
      <td>-8.173140</td>
      <td>3544.457239</td>
      <td>incongruent</td>
    </tr>
    <tr>
      <th>153</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>4</td>
      <td>...</td>
      <td>congruent</td>
      <td>0.000388</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068476</td>
      <td>-7.853632</td>
      <td>2575.069063</td>
      <td>incongruent</td>
    </tr>
    <tr>
      <th>156</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>5</td>
      <td>...</td>
      <td>incongruent</td>
      <td>0.000742</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.069494</td>
      <td>-7.206193</td>
      <td>1347.751442</td>
      <td>incongruent</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



Having done that, you can now create another table of counts in each cell of the design, like you did earlier. But, instead of `flankers` and `target`, use `flankers` and your new variable, `simon`.

<font color=blue ><h4>Q32</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.groupby(['flankers','simon'])[['rt','error']].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>rt</th>
      <th>error</th>
    </tr>
    <tr>
      <th>flankers</th>
      <th>simon</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">congruent</th>
      <th>congruent</th>
      <td>60</td>
      <td>60</td>
    </tr>
    <tr>
      <th>incongruent</th>
      <td>60</td>
      <td>60</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">incongruent</th>
      <th>congruent</th>
      <td>60</td>
      <td>60</td>
    </tr>
    <tr>
      <th>incongruent</th>
      <td>60</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>



Now we can get a bit interesting and EDA-ish. Let's look at mean RT as a function of those same two variables, `flankers` and `simon`. You can leave out `error`.

<font color=blue ><h4>Q33</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df.groupby(['flankers','simon'])[['rt']].mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>rt</th>
    </tr>
    <tr>
      <th>flankers</th>
      <th>simon</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">congruent</th>
      <th>congruent</th>
      <td>0.000415</td>
    </tr>
    <tr>
      <th>incongruent</th>
      <td>0.000418</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">incongruent</th>
      <th>congruent</th>
      <td>0.000443</td>
    </tr>
    <tr>
      <th>incongruent</th>
      <td>0.000437</td>
    </tr>
  </tbody>
</table>
</div>



Get the above cell working first. If you have the time and inclination, for bonus points, round the values to 2 decimal places (as we might want for a table in a manuscript):

<font color=blue ><h4>Q34</h4>
</font>

<font color=orange> 0/1 </font>


```python
orange = [0.]
```

Looking at either table above, does it look like our hypotheses are being supported? That is, are RTs longer (slower) for the incongruent versions of each task, and are they extra-slow for the double-incongruent condition? 

<font color=red> Double check. Which condition was hypothesized to show the longest (slowest) RT, and which condition actually did? </font>

<font color=blue> 0/1 </font>


```python
blue = blue + [0.]
```

Yes it seems that the hypothesis is being supported but the differences in rt are not as large as I expected 

### EDA

We've actually been doing a fair bit of EDA already, such as looking at histograms, descriptive statistics, and RTs by condition. But, visualization of data is often more helpful than tables like the ones above. Box plots are a nice way to look at the distribution of variables, and make some visual comparisons between conditions. 

Plot box plots of the RT data (`rt`) for each groupby condition. Remember that, just like descriptive statistics, pandas DataFrames have methods for generating plots.

[Note: there's no easy way to add titles to the sublpots, or control their arrangement (e.g., making them all appear in one row), but the plots appear in the same order as in the table you generated above]. 

<font color=blue ><h4>Q35</h4>
</font>

<font color=red> There are extra outliers in your plots due to some minor sampling errors. These would be resolved by using a single `.groupby` line as seen in previous questions just above. </font>

<font color=blue> 0.25/1 </font>


```python
blue = blue + [0.25]
```


```python
df_simon = df.groupby('simon')
df_flankers = df.groupby('flankers')
df_flankers[['rt']].plot(kind='box')
df_simon[['rt']].plot(kind = 'box')
```




    simon
    congruent      AxesSubplot(0.125,0.125;0.775x0.755)
    incongruent    AxesSubplot(0.125,0.125;0.775x0.755)
    dtype: object






![png](Assignment_3_files/Assignment_3_152_1.png)






![png](Assignment_3_files/Assignment_3_152_2.png)






![png](Assignment_3_files/Assignment_3_152_3.png)






![png](Assignment_3_files/Assignment_3_152_4.png)



---

As noted, there is no easy way to combine the `groupby()` method with options that control the layout of the box plots, add individual titles, or other fancy things. You *can* do all of this, but it requires more code, as in the example below. I've done this because it's probably a bit advanced for you to do on your own at this point, but I want you to use it in answering the questions below. 


```python
figure, axes = plt.subplots(1, 4, sharey=True, figsize=(15,5))
df['rt'].where((df['flankers']=='congruent') & (df['simon']=='congruent')).plot(ax=axes[0], kind='box', title='FC_SC')
df['rt'].where((df['flankers']=='congruent') & (df['simon']=='incongruent')).plot(ax=axes[1], kind='box', title='FC_SI')
df['rt'].where((df['flankers']=='incongruent') & (df['simon']=='congruent')).plot(ax=axes[2], kind='box', title='FI_SC')
df['rt'].where((df['flankers']=='incongruent') & (df['simon']=='incongruent')).plot(ax=axes[3], kind='box', title='FI_SI')
plt.show()
```




![png](Assignment_3_files/Assignment_3_154_0.png)



Note the one difference in the code below:


```python
figure, axes = plt.subplots(1, 4, sharey=True, figsize=(15,5))
df['invrt'].where((df['flankers']=='congruent') & (df['simon']=='congruent')).plot(ax=axes[0], kind='box', title='FC_SC')
df['invrt'].where((df['flankers']=='congruent') & (df['simon']=='incongruent')).plot(ax=axes[1], kind='box', title='FC_SI')
df['invrt'].where((df['flankers']=='incongruent') & (df['simon']=='congruent')).plot(ax=axes[2], kind='box', title='FI_SC')
df['invrt'].where((df['flankers']=='incongruent') & (df['simon']=='incongruent')).plot(ax=axes[3], kind='box', title='FI_SI')
plt.show()
```




![png](Assignment_3_files/Assignment_3_156_0.png)



What is the difference between the first and second sets of plots I generated in the cells above?

<font color=blue ><h4>Q36</h4>
</font>

<font color=red> The whiskers envelop the outliers in the second set. More importantly though, *why* are they different? Hint: "inverse".</font>

<font color=blue> 0.25/1 </font>


```python
blue = blue + [0.25]
```

The first set of plots show the presence of outliers whereas the second set just have longer "whiskers"

Compare the plots you generated with the `groupby()` method and the ones I generated above. Both are accurate representations of the data. What are some advantages of visualizing the data using the more complex code that I wrote? Try to come up with at least three.

<font color=blue ><h4>Q37</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```

(1) Side by side comparisons allow for easier analysis of the data (2) the labeling of the plots also allow for easier analysis (3) the second set of graphs have a much smaller y'axis range which gives a more exact marker of the mean/IQR/etc.

Compare the two sets of box plots I generated. Is there a visible benefit to using the inverse transform on the RT data? [
You might want to consult the [matplotlib API for its `boxplot` function](https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.pyplot.boxplot.html) if you need a reminder of what the elements of boxplots represent.]



<font color=blue ><h4>Q38</h4>
</font>

<font color=red> You actually answered this question above (where, unfortunately, it wasn't asked for) with reference to outliers. </font>

<font color=blue> 0.25/1 </font>


```python
blue = blue + [0.25]
```

The only benefit to using the inverse transform data in this case is that the box plots seem more normally-distributed. 

### Outliers

For the sake of this exercise, we will remove outliers from the raw (untransformed) RT data. A standard criterion for defining outliers, is values > 3 standard deviations from the mean. If the data are normally distributed, values > 3 SDs are quite extreme, because 3 SDs comprise 99.7% of the values in a normal distribution. 

By transforming our data to *z* scores we modify the data values so that they have a mean of zero and a standard deviation of 1. *Z* score transformations were covered in Chapter 4 of *Manipulating DataFrames with pandas*, but as a reminder the formula is:

$$z = (x - \bar{x}) / \sigma{_x}$$

In other words, you subtract the mean RT from every individual RT value and then divide the result by the standard deviation of the RT values. 

Create a new column in `df` that contains the *z*-transformed RT values. 

<font color=blue ><h4>Q39</h4>
</font>

<font color=red> Spot on!...but would still benefit from spaces between elements. </font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df['ztransform'] = (df['rt']-df['rt'].mean())/df['rt'].std()
```

Plot a histogram of the z-transformed data

<font color=blue ><h4>Q40</h4>
</font>

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```


```python
df['ztransform'].plot(kind='hist')
plt.show()
```




![png](Assignment_3_files/Assignment_3_176_0.png)



Find and list all the rows in `df` whose standard deviation is greater than 3. 

<font color=blue ><h4>Q41</h4>
</font>

<font color=red> Correct, but go for fewer lines of code next time. </font>

<font color=blue> 0.75/1 </font>


```python
blue = blue + [0.75]
```


```python
df['ztransform'] > 3
outliers = df['ztransform'].loc[df['ztransform']>3]
print(outliers)
```

    156    3.304447
    282    3.553321
    315    3.653238
    675    4.590417
    Name: ztransform, dtype: float64


Note that although normal distributions are symmetrical around a mean of 0 (in other words, the mean is zero and there are equal numbers of values below and above zero, so outliers would be both *z* scores less than -3 and greater than 3), we don't need to worry about values with SDs < -3. Why is that?

<font color=blue> 1/1 </font>


```python
blue = blue + [1.]
```

Because we can see in the histograms that there are no values with SDs < -3

### Remove outliers
Remove all rows in the DataFrame that contain `zrt` scores > 3. Hint: adapt the code that we used above to remove practice trials, but using a different operator and on a different column.

<font color=blue ><h4>Q42</h4>
</font>

<font color=red> Note the instructions read `> 3`. Therefore, your `<=` should be `<`. Thankfully, there are none that approach, must less land on, 3. </font>

<font color=blue> 0.5/1 </font>


```python
blue = blue + [0.5]
```


```python
df[df['ztransform']<= 3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>mapping</th>
      <th>messageViewingTime</th>
      <th>block</th>
      <th>trialNum</th>
      <th>...</th>
      <th>rt</th>
      <th>response</th>
      <th>error</th>
      <th>anticipation</th>
      <th>feedbackResponse</th>
      <th>targetOnError</th>
      <th>logrt</th>
      <th>invrt</th>
      <th>simon</th>
      <th>ztransform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>144</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>0.000552</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068436</td>
      <td>-7.502481</td>
      <td>1812.533282</td>
      <td>congruent</td>
      <td>1.302033</td>
    </tr>
    <tr>
      <th>147</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>0.000344</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068915</td>
      <td>-7.973836</td>
      <td>2903.976759</td>
      <td>congruent</td>
      <td>-0.880308</td>
    </tr>
    <tr>
      <th>150</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>3</td>
      <td>...</td>
      <td>0.000282</td>
      <td>white</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.066689</td>
      <td>-8.173140</td>
      <td>3544.457239</td>
      <td>incongruent</td>
      <td>-1.535191</td>
    </tr>
    <tr>
      <th>153</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>4</td>
      <td>...</td>
      <td>0.000388</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068476</td>
      <td>-7.853632</td>
      <td>2575.069063</td>
      <td>incongruent</td>
      <td>-0.417403</td>
    </tr>
    <tr>
      <th>159</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>13.251555</td>
      <td>1</td>
      <td>6</td>
      <td>...</td>
      <td>0.000427</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068581</td>
      <td>-7.759177</td>
      <td>2342.974856</td>
      <td>congruent</td>
      <td>-0.012539</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>849</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>44</td>
      <td>...</td>
      <td>0.000424</td>
      <td>white</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>0.064946</td>
      <td>-7.765370</td>
      <td>2357.530289</td>
      <td>incongruent</td>
      <td>-0.040273</td>
    </tr>
    <tr>
      <th>852</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>45</td>
      <td>...</td>
      <td>0.000446</td>
      <td>white</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.068929</td>
      <td>-7.714601</td>
      <td>2240.828107</td>
      <td>congruent</td>
      <td>0.192222</td>
    </tr>
    <tr>
      <th>855</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>46</td>
      <td>...</td>
      <td>0.000540</td>
      <td>white</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.069080</td>
      <td>-7.524544</td>
      <td>1852.968372</td>
      <td>incongruent</td>
      <td>1.175324</td>
    </tr>
    <tr>
      <th>858</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>47</td>
      <td>...</td>
      <td>0.000330</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068443</td>
      <td>-8.015840</td>
      <td>3028.551766</td>
      <td>incongruent</td>
      <td>-1.029383</td>
    </tr>
    <tr>
      <th>861</th>
      <td>spid10</td>
      <td>2014</td>
      <td>6</td>
      <td>17</td>
      <td>17</td>
      <td>44</td>
      <td>0</td>
      <td>74.063199</td>
      <td>5</td>
      <td>48</td>
      <td>...</td>
      <td>0.000431</td>
      <td>black</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.068893</td>
      <td>-7.749449</td>
      <td>2320.292634</td>
      <td>incongruent</td>
      <td>0.031372</td>
    </tr>
  </tbody>
</table>
<p>236 rows × 23 columns</p>
</div>



Confirm that this worked

<font color=blue ><h4>Q43</h4>
</font>

<font color=red> Alas, this doesn't confirm that it worked. </font>

<font color=blue> 0/1 </font>


```python
blue = blue + [0.]
```


```python
print(df['ztransform'] <=3)
```

    144     True
    147     True
    150     True
    153     True
    156    False
           ...  
    849     True
    852     True
    855     True
    858     True
    861     True
    Name: ztransform, Length: 240, dtype: bool


<div class="alert alert-block alert-success">
<b>OMG you're done!</b> Don't forget to hit "Submit" for this assignment on Teams. We'll collect all the assignments at the due date/time, but we do need your submission on Teams in order to assign a grade. Also, if you want your assignment grade to be based on work done after the due time (when we collect it), you will need to contact the instructor to request this, and the time you click "submit" on Teams will be considered your submission time for computing the late penalty.
</div>


## Grade


```python
print(blue)
len(blue)
```

    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.25, 0.25, 1.0, 0.25, 1.0, 1.0, 0.75, 1.0, 0.5, 0.0]





    43




```python
print(orange)
len(orange)
```

    [0.0]





    1




```python
Blue = np.array(blue + orange).sum()
print(Blue)
```

    34.5



```python
Grade = Blue / len(blue) * 100
print(str(Grade.round(2)) + '%')
print(str(int(Grade * 30)) + ' XP')
```

    80.23%
    2406 XP

