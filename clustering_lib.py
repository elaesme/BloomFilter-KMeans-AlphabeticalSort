import numpy as np
import pandas as pd
import random
import time


def get_data(fname):
    with open(fname, 'r') as f:
        data= list(f.readlines())

    for i in range(len(data)):
        data[i]= data[i][:-1]
        data[i]= list(map(float, data[i].split(',')))
    
    features=['Target', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash' , 'Magnesium', 'Total phenols', 
        'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 
        'OD280/OD315 of diluted wines','Proline']

    dataf= pd.DataFrame(data, columns=features)

    dataf.drop(['Target'], axis = 1, inplace= True)

    return dataf



def normalize(data):
    normalized= data.copy()
    summary= normalized.describe()
    for col in normalized.columns:
        normalized[col]= (normalized[col]-summary[col]['mean'])/summary[col]['std']
    return normalized


def euclidean_distance(x, y):
    '''Euclidean distance between two points'''
    return np.sqrt(((x - y)**2).sum())



def choose_centroids(normalized, k):
    ''' In this way we pick at random k centers from the dataset'''
    lista=[i for i in range(178)]
    ind=[]
    for i in range(k):
        ind.append(random.choice(lista))
    centroids=[]
    for el in range(len(ind)):
        centroids.append(list(normalized.loc[el]))
    return centroids


def difference(list1, list2):
    diff=[]
    for i in range(len(list1)):
        diff.append(list1[i]-list2[i])
    return diff


def square(list):
    return [i ** 2 for i in list]


def division(lista, el):
    for i in range(len(lista)):
        lista[i]= lista[i]/el
    return lista


def move_centers(clus1):
    b=dict()
    for el in clus1.keys():
        summ=[sum(x) for x in zip(*clus1[el])]
        b[el]=division(summ, len(clus1[el]))
    return b


def update_clusters(new_centers, normalized):
    distances=dict()
    for k in range(178):
    # d is the distance of each point from the three clusters (d=[distance_from_cluster1, distance_from_cluster2, distance_from_cluster3])
        d=[]
        for i in range(3):      
            X=list(normalized.loc[k])
            dist_point_center=sum(square(difference(X, new_centers[i])))
        
            d.append(dist_point_center)
        distances[k]=d
    clusters={i:[] for i in range(3)}
    
    for el in distances.keys():
        ii = distances[el].index(min(distances[el]))
        clusters[ii].append(list(normalized.loc[el]))
        
    return clusters

def update_clusters2(new_centers, normalized):
    distances=dict()
    for k in range(178):
    # d is the distance of each point from the three clusters (d=[distance_from_cluster1, distance_from_cluster2, distance_from_cluster3])
        d=[]
        for i in range(3):      
            X=list(normalized.loc[k])
            dist_point_center=sum(min(X, new_centers[i]))//sum(max(X, new_centers[i]))
        
            d.append(dist_point_center)
        distances[k]=d
    clusters={i:[] for i in range(3)}
    
    for el in distances.keys():
        ii = distances[el].index(min(distances[el]))
        clusters[ii].append(list(normalized.loc[el]))
        
    return clusters

def kMeans(k, n_iter, normalized, centroids):
    start = time.time()

    distances=dict()
    for k in range(178):
        # d is the distance of each point from the three clusters (d=[distance_from_cluster1, distance_from_cluster2, distance_from_cluster3])
        d=[]
        for i in range(3):      
            X=list(normalized.loc[k])
            dist_point_center=sum(square(difference(X, centroids[i])))

            d.append(dist_point_center)
        distances[k]=d
    clusters={i:[] for i in range(3)}

    for el in distances.keys():
        ii=distances[el].index(min(distances[el]))
        clusters[ii].append(list(normalized.loc[el]))
    
    for _ in range(n_iter):
        new_centers= move_centers(clusters)
        clusters= update_clusters(new_centers, normalized)
    end = time.time()
    print('Execution time: ', end-start)
    return clusters


def kMean2(k, n_iter, normalized, centroids):
    start = time.time()
    EuclidianDistance=np.array([]).reshape(178,0)
    
    distances=dict()
    for k in range(178):
        # d is the distance of each point from the three clusters (d=[distance_from_cluster1, distance_from_cluster2, distance_from_cluster3])
        d=[]
        for i in range(3):      
            X=list(normalized.loc[k])
            
            dist_point_center=sum(min(X, centroids[i]))//sum(max(X, centroids[i]))
            d.append(dist_point_center)
        distances[k]=d
    clusters={i:[] for i in range(3)}

    for el in distances.keys():
        ii=distances[el].index(min(distances[el]))
        clusters[ii].append(list(normalized.loc[el]))
    
    for _ in range(n_iter):
        new_centers= move_centers(clusters)
        clusters= update_clusters2(new_centers, normalized)
    end = time.time()
    print('Execution time: ', end-start)
    return clusters