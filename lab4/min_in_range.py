def find_min_in_range(array,start,end):
    min = array[start]
    for i in range(start+1,end):
        if array[i] < min:
            min = array[i]
    return min

a = [3,4,5,6,1,10,12,13,5,50,0]

min_a = find_min_in_range(a,5,9)
print(min_a)
