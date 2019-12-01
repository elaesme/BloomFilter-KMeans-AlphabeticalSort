# Import the necessary libraries

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import clustering_lib
import time
import warnings
warnings.filterwarnings('ignore')

def predicted_clust(data,cluster):
    clu=[]
    for i in range(len(data)):
        for j in range(3):
            if list(data.loc[i]) in cluster[j]:
                clu.append(j)
    return clu

def actual_clust():
    with open('wine.data', 'r') as f:
        data= list(f.readlines())

    for i in range(len(data)):
        data[i]= data[i][:-1]
        data[i]= list(map(float, data[i].split(',')))

    features=['Target', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash' , 'Magnesium', 'Total phenols',
            'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue',
            'OD280/OD315 of diluted wines','Proline']

    wine= pd.DataFrame(data, columns=features)

    lista = list(wine["Target"])
    for i in range(len(lista)):
        if int(lista[i])==1:
            lista[i]=0
        elif int(lista[i])==2:
            lista[i]=1
        elif int(lista[i])==3:
            lista[i]=2

    return lista

def print_result(data):
    actual = data["actual"]
    predicted = data["predicted"]
    acc = accuracy_score(actual, predicted)
    summary = classification_report(actual, predicted)
    results = confusion_matrix(actual, predicted)
    print ('Confusion Matrix :')
    print(results)
    print ('Accuracy Score: ',acc)
    print ('Summary : ')
    print (summary)

# Prepare the data for both clustering
dataf = clustering_lib.get_data('wine.data')
K=3  #K to be decided with the elbow method
# For built-in Kmeans function:
normalized= clustering_lib.normalize(dataf)
centroids= clustering_lib.choose_centroids(normalized, K)

# For K-means++
normalized2 = clustering_lib.normalize(dataf)

# Now Lets run both K-means and see the execution time for both
# Built-in K-means
cluster1 = clustering_lib.kMeans(3,1000,normalized, centroids)

# K-means++
start2 = time.time()
cluster2 = KMeans(n_clusters = 3, init = 'k-means++', n_init = 1000).fit(normalized2)
end2 = time.time()
print('Excecution Time Kmeans++: ', end2-start2)

# prepare the actual and predicted classes to compare the result of clustering
# Getting predicted and actual cluster from build in Kmeans
normalized["predicted"] = predicted_clust(normalized, cluster1)
normalized["actual"] = actual_clust()

# Getting predicted and actual cluster from Kmeans++
normalized2["predicted"] = cluster2.predict(normalized2)
normalized2["actual"] = actual_clust()

# we need to tranform the label of the predicted cluster in kmeans++ before we measure the performance
res = normalized2['predicted']
for k, v in enumerate(res):
    if v == 2: res[k] = 1
    elif v == 1: res[k] = 2

# measure the performance of both Kmeans by looking at confusion matrix and calculate the accuracy
# For built-in Kmeans
print_result(normalized)

# For Kmeans++
print_result(normalized2)
