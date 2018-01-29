import string

file_object = open("words.txt", 'r')
content = file_object.read()
content = content.lower()
for c in string.punctuation:
    content = content.replace(c,"")
content = content.split()
cnt=0
for word in content:
    if word=='many':
        cnt+=1
print("number of times that we got many:",cnt)