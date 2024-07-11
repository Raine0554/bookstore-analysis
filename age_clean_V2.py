import pandas as pd
#import matplotlib.pyplot as plt
import re

def age_clean():
    users = pd.read_csv(r"data/BX-Users.csv")
    users = users.dropna(subset=['User-Country'])

    def remove_punctuation(text):
        text = text.strip()
        return re.sub(r'[^\w\s]', '', text)

    users['User-Country'] = users['User-Country'].apply(remove_punctuation)
    full_count = users.value_counts("User-Country").reset_index()
    full_count.columns = ['User-Country', 'Count']
    top_50 = full_count.head(50)
    # create top 50 countries
    users_50 = users[users['User-Country'].isin(top_50['User-Country'])]
    
    # drop all missing values
    users_50 = users_50.dropna(subset=['User-Age'])
    # convert age column to integers
    users_50['User-Age'] = users_50['User-Age'].astype(int)
    # find median for whole dataset and country specific    
    median_age_by_country = users_50.groupby('User-Country')['User-Age'].median().reset_index()
    # find the mean of the country median and total median then return as int
    median_age_by_country['Weighted-Age'] = ((median_age_by_country['User-Age'])).astype(int)
    median_age_by_country = median_age_by_country.drop(columns=['User-Age'])

    # merge median age and users file for later computation
    age_merged = pd.merge(users_50, median_age_by_country, on='User-Country')
    #catch errors like missing, 0 or >116
    age_merged['User-Age'] = age_merged['User-Age'].fillna(age_merged['Weighted-Age'])
    mask = age_merged['User-Age'] == 0
    age_merged.loc[mask, 'User-Age'] = age_merged.loc[mask, 'Weighted-Age']
    mask2 = age_merged['User-Age'] > 116
    age_merged.loc[mask2, 'User-Age'] = age_merged.loc[mask2, 'Weighted-Age']

    # remove extra columns and catch non-int types
    age_merged = age_merged.drop(columns=['Weighted-Age'])
    age_merged['User-Age'] = age_merged['User-Age'].astype(int)

    #for visualising the data 
    """plt.boxplot(age_merged['User-Age'])
    plt.ylabel('Age')
    plt.title('Minimal Imputation Dataset Age Distribution')
    plt.yticks(range(0, 120, 20))
    plt.grid(True)
    plt.show()"""
    return age_merged



