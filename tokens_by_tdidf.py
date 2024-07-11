# TOP 10 MOST COMMON TOKENS BY TD IDF
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt 
import pandas as pd

from book_title_tokenise import tokenise_titles

def common_tokens():
    books = tokenise_titles()
    books['Title-Tokens'] = books['Title-Tokens'].apply(lambda x: ' '.join(x))
    vectorizer = TfidfVectorizer()
    TD_IDF = vectorizer.fit_transform(books['Title-Tokens'])

    # getting the words from the TF-IDF vectorizer
    feature_names = vectorizer.get_feature_names_out()
    tdidf_df = pd.DataFrame(TD_IDF.toarray(), columns=feature_names)

    # Eliminating useless token words
    naughty_tokens = ['novel', 'paperback', 'book', 'story']
    tdidf_df_clean = tdidf_df.drop(naughty_tokens, axis='columns')

    # calculating the mean TF-IDF score for each word across all documents
    mean_tdidf_scores = tdidf_df_clean.mean(axis=0)
    sorted_tokens = mean_tdidf_scores.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sorted_tokens[:10].plot.bar(color='skyblue', width=0.7)
    plt.xlabel('Token')
    plt.ylabel('TD IDF')
    plt.title('Top 10 Most Common Title Tokens (By TD IDF)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


common_tokens()
