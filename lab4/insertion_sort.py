def insertion_sort(array):
    d = len(array)
    for i in range(1,d):
        j = i
        while array[j] < array[j-1]:
            tmp = array[j-1]
            array[j-1] = array[j]
            array[j] = tmp
            j -= 1
            if j == 0:
                break
    return array

a = [3,5,7,1,2,0,4]

b  = insertion_sort(a)
print (b)