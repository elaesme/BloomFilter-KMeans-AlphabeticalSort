def counting_sort (lists):
    k = max(lists)
    aux_size = k + 1
    aux = [0] * aux_size
    for item in lists:
        # occurances
        aux[item] += 1
    i = 0
    for item in range(aux_size):
        for a in range(aux[item]):
            lists[i] = item
            i += 1
    return lists

