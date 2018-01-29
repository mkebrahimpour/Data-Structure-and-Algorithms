c = input ("Enter a character:\n")
n = input ("Enter a number, -1 for drawing a line and -2 to stop\n")
n = int(n)
while n!=-2:
    if n!=-1:
        for i in range(n):
            print(c,end="")
    else:
        print("--------oooooooo----------\n")
    c = input("\nEnter a character:\n")
    n = input("Enter a number, -1 for drawing a line and -2 to stop\n")
    n = int(n)