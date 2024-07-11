import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

from k_means_date import k_means_of_date_age_rating

def elbow():
    data = k_means_of_date_age_rating().drop(columns="ISBN")
    distortions = []
    k_range = range(1, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)
        distortions.append(kmeans.inertia_) 
        
    plt.plot(k_range, distortions, 'bx-')

    plt.title('The Elbow Method showing the optimal k')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.show()

elbow()
