import sys
import pandas as pd
import numpy as np
import difflib

#python3 average_ratings.py movie_list.txt movie_ratings.csv output.csv
#filename1 = sys.argv[1]
#filename2 = sys.argv[2]
#filename3 = sys.argv[3]
filename1 = "movie_list.txt"
filename2 = "movie_ratings.csv"


titles = open(filename1).read().split('\n')
title_data = pd.DataFrame(data = titles, columns=['Title'])
#print(title_data)
ratings = pd.read_csv(filename2)
#print(ratings)

def average(movie):
    # Inspired from https://docs.python.org/3/library/difflib.html#difflib.get_close_matches
    matched = pd.Series(data=difflib.get_close_matches(movie, ratings['title'], n = 30, cutoff = 0.6))
    #print(matched)
    # and https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
    avg_rating = round(ratings[ratings['title'].isin(matched)]['rating'].mean(), 2)
    #print(avg_rating)
    return avg_rating

title_data['Ratings'] = title_data['Title'].apply(average)
title_data = title_data[np.isnan(title_data['Ratings'])==False]
print(title_data)

#title_data.to_csv(filename3)