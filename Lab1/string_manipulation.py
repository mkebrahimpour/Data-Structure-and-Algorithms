str = input("please insert a word:'\n")
STR = []
STR.append(str)
while str!='quit':
    if len(str)==1:
        for word in STR:
            if word[0]==str:
                print(word)
        str = input("please insert as word:\n")

    else:
        print(str)
        str = input("please insert as word:\n")
        if len(str)>1:
            STR.append(str)

