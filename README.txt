README for assignment 2 project code

Descriptions
---------------
This repository contains 5 main codes and 5 supplimentary codes


# library requirements #

librarys required
- pandas
- matplotlib.pyplot
- ast
- scipy.stats
- sklearn.cluster
- nltk
- re
- sklearn.feature_extraction.text
-


# main project codes #

3d K means plot
--------------------------------------------------
to produce a 3d plot visualisation of the k means clustering on 
User-Age, Book-Rating and Year-Of-Publication, follow these steps:

requirements
- python files: "age_clean_V2", "date_cleaning.py", "rating_clean.py"
                and "k_means_date.py" need to be in the same directory
                as "3d_plot.py"
- datasets: the data folder containing the origonal BX-datasets must also 
            be in the same directory as "3d_plot.py"

With the requirements met creating the 3d plot will simply need
the execution of the script "3d_plot.py"


2d K means plots
--------------------------------------------------
to produce a series of 2d plots for an alternate visualisation of 
the k means clustering on User-Age, Book-Rating and Year-Of-Publication, 
follow these steps:

requirements
- python files: "age_clean_V2", "date_cleaning.py", "rating_clean.py"
                and "k_means_date.py" need to be in the same directory
                as "2d_plot.py"
- datasets: the data folder containing the origonal BX-datasets must also 
            be in the same directory as "2d_plot.py"

With the requirements met creating the 2d plots will simply need
the execution of the script "2d_plot.py"


elbow method grpah for K means
--------------------------------------------------
produce elbow graph for K means for the BX-datasets

requirements
- python files: "age_clean_V2", "date_cleaning.py", "rating_clean.py"
                and "k_means_date.py" need to be in the same directory
                as "elbow.py"
- datasets: the data folder containing the origonal BX-datasets must also 
            be in the same directory as "elbow.py"

With the requirements met creating the elbow graph will simply need
the execution of the script "elbow.py"


Title-Ratings
--------------------------------------------------
To produce series of graphs for the Title words a age population might enjoy 
based on the correlation. 

requirements
- python files: "age_clean_V2" and "book_title_tokenise.py" need to be placed 
                in the same directory as "Title-Ratings.py"
- datasets: the data folder containing the origonal BX-datasets must also 
            be in the same directory as "Title-Ratings.py"
- "book_title_tokenise.py": will require serveal install lines at the start of
                            the program to be uncommented on the first run of   
                            "Title-Ratings.py"


With the requirements met creating the series of charts will simply need
the execution of the script "Title-Ratings.py"


Common tokens
--------------------------------------------------
To produce a graph displaying the top ten title words by TD IDF

requirements
- python files: "book_title_tokenise.py" need to be placed 
                in the same directory as "tokens_by_tdidf.py"
- datasets: the data folder containing the origonal BX-datasets must also 
            be in the same directory as "tokens_by_tdidf.py"
- "book_title_tokenise.py": will require serveal install lines at the start of
                            the program to be uncommented on the first run of   
                            "tokens_by_tdidf.py"


With the requirements met creating the graph will simply need
the execution of the script "tokens_by_tdidf.py"