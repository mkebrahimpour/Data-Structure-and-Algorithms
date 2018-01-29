def prime(n):
    arr = [1,2]
    for i in range(3,n):
        cnt = 0
        for j in range(i-1,1,-1):
            check_sum = len(range(i-1,1,-1))
            if i % j != 0:
                cnt+=1
        if cnt == check_sum:
            arr.append(i)
    return arr

num = input("please insert an interger:\n")
num = int(num)
res = prime(num)
for ind in range(len(res)):
    print(res[ind])
