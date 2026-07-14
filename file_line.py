file=open("text3.txt","r")
counter=0
content=file.read()
colList=content.split("\n")
for i in colList:
    if i:
        counter+=1
print("no of line in the file")
print(counter)
file.close()
with open("text3.txt","r") as file:
    data =file.readlines()
    for line in data:
        word=line.split()
        print(word)