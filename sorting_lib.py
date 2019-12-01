def counting_sort (lists):
    k = max(lists)
    aux_size = k + 1
    # temp list to store th
    aux = [0] * aux_size
    for item in lists:
        # calculate occurance
        aux[item] += 1
    i = 0
    # sort the element
    for item in range(aux_size):
        for a in range(aux[item]):
            lists[i] = item
            i += 1
    return lists

def counting_sort_2 (lists):
    #Prepare temporary list, one to accomodate the ord() indexes and ordering the input
    # 127 is the maximum allocation of ascii tabe that contain latin letters
    # source : http://www.asciitable.com/
    temp = aux = [0] * 127
    # build a result list
    result = [""] * len(lists)
    # calculate the occurance
    for item in lists:
        aux[ord(item)] += 1
    #update the aux list
    for i in range(127):
        aux[i] += aux[i-1]
    for i in range(len(lists)):
        #fill each element of the list based on ord() value of aux list
        temp[aux[ord(lists[i])]-1] = lists[i]
        #update the value of aux list, count out for each process
        aux[ord(lists[i])] -= 1
    # return the result
    for item in range(len(lists)):
        result[item] = temp[item]
    return result

