size = input("input the size of the array:\n")
size = int (size)
list = []
def fillUp(list,size):
    for ind in range(size):
        list.append(ind)

def print_arr (list):
    for ind in range(len(list)):
        print(list[ind])

def printPos(list,pos):
    print(list[pos])

fillUp(list,size)
print_arr(list)
printPos(list,5)