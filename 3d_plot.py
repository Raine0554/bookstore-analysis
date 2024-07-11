from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from k_means_date import k_means_of_date_age_rating

def plot_3d():
    data = k_means_of_date_age_rating()

    clusters = KMeans(n_clusters=3)
    clusters.fit(data[['Year-Of-Publication', 'User-Age', 'Clean-Book-Rating']])

    colormap = {0: 'red', 1: 'green', 2: 'blue'}
        
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter(data['Year-Of-Publication'], 
               data['User-Age'], 
               data['Clean-Book-Rating'],
               c=[colormap.get(x) for x in clusters.labels_])
        
    ax.set_ylabel('User-Age')
    ax.set_xlabel('Year-Of-Publication')
    ax.set_zlabel('Clean-Book-Rating')
    ax.set_title(f"k = {len(set(clusters.labels_))}")
        
    plt.show()

    return

plot_3d()