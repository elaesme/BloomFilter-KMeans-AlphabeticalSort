# Algorithmic Methods for Data Mining - Homework 4
# *Hard coding*
**Goal of the homework**: write important algorithms and function from scratch.

Made by Group #6, also known as: *Sabriye Ela Esme, Octavianus Surya Putra 
Sinaga*, and *Flaminia Spasiano*.

This repository contais:
* `hashing_lib.py`: a python module that contains all the functions we've used to build the bloom filter.
* `main.ipynb`: a Jupyter notebook explaines choices we've made throughout the homework. 
* `sorting_lib.py`: a python module that contains all the functions we've used for task 2.
* `clustering_lib.py`: a python module that contains all the functions we've used for task 3.
* `theoretical_lib.py`: a python module to answer the theoretical question in task 4
* ` main.ipynb`: a python notebook that collects all the choices we made, explains how the funcions we wrote are usefull and visualize the clustering for task3


## 1. Hashing task!
For this task we've built three hash functions, necessary to implement the Bloom Filter. 

In the `hashing_lib.py` are contained our hash functions: 
1. One is a particular implementation of an hash function based on Fibonacci hashing method.
2. For another one, we took inspiration form a famous hash function (SHA256), which is very fast and it's often used in cryptographic protocols.
3. One takes advantage of the particular construction of each password.
4. The last one takes the sum of the corresoinging ASCII number of each character, square it and return that number modulo 10**8

To implement our Bloom Filter structure we've dediced to build the filter as a bitarray. The big thing we want to control when creating our bloom filter is our false positive rate. To do this we'll need to have an idea of the size of our data set.

The formula to calculate the size of your bit array (m = size of bit array, n = expected number of items, and p = probability percentage represented as a decimal, k= number of hash function used):
* `m=  -n log(p)/ log(2)^2 `

The formula to calculate the number of hashes to use (k = number of hashes to use):
* `k=  - (m log(2))/n `


## 2. Alphabetical Sort
For thid task, we implement counting sort algorithm to sort list of words alphabetically.

In `sorting_lib.py`, there are three function:
1. Basic Counting sort: sorting list of integer with counting sort algorithm
2. Sorting all the letters in the alphabetically based on counting sort algorithm
3. Sorting list of word alphabetically based on counting sort algorithm

## 3. Find similar wines!
For this task we implemented our personal Kmeans clustering algorithm. The `clustering_lib` module contains the functions used to build kMeans, the functions used to build another implementations of Kmeans (*K-Means Min Max*, which is very similar to the first one, but it uses a different type of distance to measure distances between a point and a center of a cluster)

For the implemetation of kmeans in Map Reduce we used the same strategy used before but as output of the kmeans_Map_Reduce, since a list cannot be the key of a dictionary in Python, we have a list o list: each element is the tuple (list=coordinates of the center of the cluster, an integer that represent the index of the row in the  dataframe (normalized) that contains the point )

## 4. K-means can go wrong!
For this task we try to prove that with different initialization of centroid, Kmeans clustering algorithm can cost the algorithm more. We compare built-in Kmeans function in `clustering_lib.py` (randomize centroid initialization) with Kmean++ algorithm(improved centroid initialization). The metrics we use to compare the result are: time execution and clustering performance. the result shown in `theoretical_lib.py`also in `main.ipynb`.
