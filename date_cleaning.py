import pandas as pd

def date_cleaning():

    books = pd.read_csv(r'data/BX-Books.csv')

    valid_books = books.loc[(books['Year-Of-Publication'] > 0) & (books['Year-Of-Publication'] < 2025)]

    return valid_books



