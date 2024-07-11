import pandas as pd
import matplotlib.pyplot as plt


def rating_cleaning():

    ratings = pd.read_csv(r'data/BX-Ratings.csv')

    # only collect number values aswell as remove excess characters
    # ratings outside 1-10 inclusive are assigned 0 for the moment
    ratings.insert(3, 'Clean-Book-Rating', ratings['Book-Rating'].apply(lambda x: int('0' + ''.join(filter(str.isdigit, str(x))))))

    # mean inputation
    mean_rating = round((ratings.loc[ratings['Clean-Book-Rating'] > 0])['Clean-Book-Rating'].mean())
    
    def replace_with_mean(value):
        if value == 0:
            return mean_rating
        
        return value
    
    ratings['Clean-Book-Rating'] = ratings['Clean-Book-Rating'].apply(replace_with_mean)

    return ratings

def produce_box_plot():
    # shown that there are no outlisers in the rating data

    ratings = pd.read_csv('data\BX-Ratings.csv')

    fig, axs = plt.subplots()

    axs.boxplot(ratings['Book-Rating'])
    axs.set_ylabel("Book Rating (1-10)")
    axs.set_xticklabels(["ratings"])
    axs.set_title("Rating data without any preprocessing")
    plt.show()
    



