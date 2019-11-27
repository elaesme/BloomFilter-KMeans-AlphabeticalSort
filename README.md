# Algorithmic Methods for Data Mining - Homework 4
# *Hard coding*
**Goal of the homework**: write important algorithms and function from scratch.

Made by Group #6, also known as: *Sabriye Ela Esme, Octavianus Surya Putra 
Sinaga*, and *Flaminia Spasiano*.

This repository contais:
* `hashing_lib.py`: a python module that contains all the hash functions we've used to build the bloom filter.
* `main.ipynb`: a Jupyter notebook explaines choices we've made throughout the homework. 


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


# Alphabetical Sort

To be commented
