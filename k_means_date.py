import pandas as pd
from matplotlib import pyplot as plt

from age_clean_V2 import age_clean
from date_cleaning import date_cleaning
from rating_clean import rating_cleaning

def k_means_of_date_age_rating():
    # first thing to do is comvine the datasets, so that each book,
    # has an average age and average rating

    users = age_clean()
    books = date_cleaning()
    ratings = rating_cleaning()

    # combine users age and ratings
    age_ratings_merged = pd.merge(users, ratings, on='User-ID', how='left')
    books.insert(5, 'Average-Age', None)
    books.insert(6, 'Average-Rating', None)
    #print(age_ratings_merged)
    avg_age_and_rating = age_ratings_merged.groupby('ISBN')[['User-Age', 'Clean-Book-Rating']].mean()
    
    age_ratings_and_books = pd.merge(books[['ISBN', 'Year-Of-Publication']], avg_age_and_rating, on='ISBN', how='left')
    age_ratings_and_books = age_ratings_and_books.dropna()
    #print(age_ratings_and_books)
    return age_ratings_and_books


