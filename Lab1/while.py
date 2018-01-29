inp = input("please write in a positive integer number...")
inp = int(inp)
while(inp != -1):
    if inp> 0 :
        if inp % 2 == 0:
            print("Even")
        else:
            print("Odd")

    inp = input("please write in a positive integer number...")
    inp = int(inp)