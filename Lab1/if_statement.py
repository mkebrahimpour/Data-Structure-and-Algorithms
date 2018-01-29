

inp = input("please write in a positive integer number.")
inp = int(inp)

if inp> 0 :
    if inp % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("you've entered a non positive integer number, try again")