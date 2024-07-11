import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# uncomment below lines on first run

#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('stopwords')


def tokenise_titles():

    books = pd.read_csv(r'data/BX-Books.csv')

    def token_sentence(title):
        lowered = title.casefold()
        special_full_stop = re.sub(r'\.(?=\w)', '. ', lowered)
        no_punct = re.sub(r'[^A-z\s]', '', special_full_stop)
        tokens = nltk.word_tokenize(no_punct)

        # remove stop words
        stop_words = set(stopwords.words('english'))
        no_stopwords = [w for w in tokens if not w in stop_words]

        # run lemmetiser
        lemmatizer = WordNetLemmatizer()
        lemmatized = [lemmatizer.lemmatize(w) for w in no_stopwords]

        return lemmatized

    books.insert(5, 'Title-Tokens', books['Book-Title'].apply(token_sentence))
    
    return books

