from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from k_means_date import k_means_of_date_age_rating

def plot_2d(x_axis, y_axis, data, clusters, ax):
    

    colormap = {0: 'red', 1: 'green', 2: 'blue'}
        

    ax.scatter(data[x_axis], 
               data[y_axis], 
               c=[colormap.get(x) for x in clusters.labels_])
        
    ax.set_ylabel(y_axis)
    ax.set_xlabel(x_axis)
    ax.set_title(f"k = {len(set(clusters.labels_))}")

    return 

def map_2d():
    data = k_means_of_date_age_rating()

    clusters = KMeans(n_clusters=3)
    clusters.fit(data[['Year-Of-Publication', 'User-Age', 'Clean-Book-Rating']])
    
    plt.rcParams.update({'figure.figsize':(13,5), 'figure.dpi':100})
    fig, axis = plt.subplots(1,3)
    plot_2d('Year-Of-Publication', 'User-Age', data, clusters, axis[0])
    plot_2d('Year-Of-Publication', 'Clean-Book-Rating', data, clusters, axis[1])
    plot_2d('User-Age', 'Clean-Book-Rating', data, clusters, axis[2])
    plt.tight_layout() 
    plt.show()
    return

map_2d()