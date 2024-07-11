import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from book_title_tokenise import tokenise_titles
from age_clean_V2 import age_clean


def title_under_45(ax1, ax2):
    books= tokenise_titles()
    ratings = pd.read_csv(r"data/BX-Ratings.csv")
    users = age_clean()
    bad_words = ['novel', 'paperback', 'book', 'story']
    # Merge all df and explode tokens
    merged_df = pd.merge(books, ratings, on='ISBN')
    merged_df = pd.merge(merged_df, users, on='User-ID')
    #merged_df['Title-Tokens'] = merged_df['Title-Tokens'].apply(literal_eval)
    jihad_df = merged_df.explode('Title-Tokens')
    jihad_df = jihad_df[~jihad_df['Title-Tokens'].isin(bad_words)]
    # Find 500 most reviewed words
    full_count = jihad_df.value_counts("Title-Tokens").reset_index()
    full_count.columns = ['Title-Tokens', 'Count']
    top_500 = full_count[full_count['Count'] >= 500]
    jihad_50 = jihad_df[jihad_df['Title-Tokens'].isin(top_500['Title-Tokens'])]
    jihad_50 = jihad_50[jihad_50['User-Age'] <= 45]
    # Find the mean for each word in each age group
    median_rating = jihad_50.groupby(['User-Age', 'Title-Tokens'])['Book-Rating'].median().reset_index()
    # Create dictionary with the corr coef for each word
    word_corr = {}
    for index, row in top_500.iterrows():
        word = row['Title-Tokens']
        word_df = median_rating[median_rating['Title-Tokens'] == word]
        word_p = spearmanr(word_df['User-Age'], word_df['Book-Rating'])
        if word_p.pvalue <= 0.05:
            word_corr[word] = word_df['User-Age'].corr(word_df['Book-Rating'], method='spearman')

    # Make dic to df
    word_corr_df = pd.DataFrame.from_dict(word_corr, orient='index', columns=['calculation_result'])
    sorted_word_corr = word_corr_df.sort_values(by=['calculation_result'], ascending=False)
    sorted_word_corr.reset_index(inplace=True)
    sorted_word_corr.columns = ['Title-Tokens', 'calculation_result']

    # Top 10 for older and younger
    top_corr = sorted_word_corr[sorted_word_corr['calculation_result'] > 0]

    bottom_corr = sorted_word_corr[sorted_word_corr['calculation_result'] < 0]
    bottom_corr['calculation_result'] = bottom_corr['calculation_result']*-1
    bottom_corr = bottom_corr.sort_values(by=['calculation_result'], ascending=False)

    ax1.bar(top_corr['Title-Tokens'], top_corr['calculation_result'])
    ax1.set_xlabel('Title-Tokens')
    ax1.set_ylabel('Correlation Coeffient')
    ax1.set_title('Correlation Coeffient for Words Older People Enjoy (Under 45)')

    
    ax2.bar(bottom_corr['Title-Tokens'], bottom_corr['calculation_result'])
    ax2.set_xlabel('Title-Tokens')
    ax2.set_ylabel('Correlation Coeffient')
    ax2.set_title('Correlation Coeffient for Words Younger People Enjoy (Under 45)')

def whole_title_rating(ax1, ax2):
    books=tokenise_titles()
    ratings = pd.read_csv(r"data/BX-Ratings.csv")
    users = age_clean()
    bad_words = ['novel', 'paperback', 'book', 'story']
    # Merge all df and explode tokens
    merged_df = pd.merge(books, ratings, on='ISBN')
    merged_df = pd.merge(merged_df, users, on='User-ID')
    jihad_df = merged_df.explode('Title-Tokens')
    jihad_df = jihad_df[~jihad_df['Title-Tokens'].isin(bad_words)]
    # Find 500 most reviewed words
    full_count = jihad_df.value_counts("Title-Tokens").reset_index()
    full_count.columns = ['Title-Tokens', 'Count']
    top_500 = full_count[full_count['Count'] >= 500]
    jihad_50 = jihad_df[jihad_df['Title-Tokens'].isin(top_500['Title-Tokens'])]

    # Find the mean for each word in each age group
    median_rating = jihad_50.groupby(['User-Age', 'Title-Tokens'])['Book-Rating'].median().reset_index()
    sorted_rating = median_rating.sort_values(by=['User-Age', 'Book-Rating'], ascending=False)

    # Create dictionary with the corr coef for each word
    word_corr = {}
    for index, row in top_500.iterrows():
        word = row['Title-Tokens']
        word_df = median_rating[median_rating['Title-Tokens'] == word]
        #word_corr[word] = word_df['User-Age'].corr(word_df['Book-Rating'], method='spearman')
        word_p = spearmanr(word_df['User-Age'], word_df['Book-Rating'])
        if word_p.pvalue <= 0.05:
            word_corr[word] = word_df['User-Age'].corr(word_df['Book-Rating'], method='spearman')

    # Make dic to df
    word_corr_df = pd.DataFrame.from_dict(word_corr, orient='index', columns=['calculation_result'])
    sorted_word_corr = word_corr_df.sort_values(by=['calculation_result'], ascending=False)
    sorted_word_corr.reset_index(inplace=True)
    sorted_word_corr.columns = ['Title-Tokens', 'calculation_result']

    # Top 10 for older and younger
    top_corr = sorted_word_corr[sorted_word_corr['calculation_result'] > 0]

    bottom_corr = sorted_word_corr[sorted_word_corr['calculation_result'] < 0]
    bottom_corr['calculation_result'] = bottom_corr['calculation_result']*-1
    bottom_corr = bottom_corr.sort_values(by=['calculation_result'], ascending=False)

    ax1.bar(top_corr['Title-Tokens'], top_corr['calculation_result'])
    ax1.set_xlabel('Title-Tokens')
    ax1.set_ylabel('Correlation Coeffient')
    ax1.set_title('Correlation Coeffient for Words Older People Enjoy')


    ax2.bar(bottom_corr['Title-Tokens'], bottom_corr['calculation_result'])
    ax2.set_xlabel('Title-Tokens')
    ax2.set_ylabel('Correlation Coeffient')
    ax2.set_title('Correlation Coeffient for Words Younger People Enjoy')


def main_titles():
    plt.rcParams.update({'figure.figsize':(13,11), 'figure.dpi':100})
    fig, axis = plt.subplots(2,2)
    title_under_45(axis[0, 0], axis[0, 1])
    whole_title_rating(axis[1, 0], axis[1, 1])
    plt.tight_layout() 
    plt.xticks(rotation=45)
    plt.show()

main_titles()
