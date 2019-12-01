def kMeans_Map_Reduce(k, n_iter, normalized, centroids):
    distances = dict()
    for k in range(178):
        # d is the distance of each point from the three clusters (d=[distance_from_cluster1, distance_from_cluster2, distance_from_cluster3])
        d = []
        for i in range(3):
            X = list(normalized.loc[k])
            dist_point_center = sum(clustering_lib.square(clustering_lib.difference(X, centroids[i])))

            d.append(dist_point_center)
        distances[k] = d
    clusters = {i: [] for i in range(3)}

    for el in distances.keys():
        ii = distances[el].index(min(distances[el]))
        clusters[ii].append(list(normalized.loc[el]))

    for _ in range(n_iter):
        new_centers = clustering_lib.move_centers(clusters)
        clusters = clustering_lib.update_clusters(new_centers, normalized)

    map_reduce = []
    for i in range(3):
        for j in range(len(clusters[i])):
            for k in range(len(normalized)):
                if list(normalized.iloc[k]) == clusters[i][j]:
                    map_reduce.append([new_centers[i], k])

    return map_reduce

centroidss= clustering_lib.choose_centroids(normalized, K)  # centroids are a list in which elements is the list of coordinates of each center
map_reduce = kMeans_Map_Reduce(3, 100, normalized, centroidss)