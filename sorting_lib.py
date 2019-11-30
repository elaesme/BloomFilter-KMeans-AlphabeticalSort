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

def counting_sort_2 (lists):
    temp = aux = [0] * 256
    result = ["" for _ in lists]
    for item in lists:
        aux[ord(item)] += 1
    for i in range(256):
        aux[i] += aux[i-1]
    for i in range(len(lists)):
        temp[aux[ord(lists[i])]-1] = lists[i]
        aux[ord(lists[i])] -= 1
    for item in range(len(lists)):
        result[item] = temp[item]
    return result

