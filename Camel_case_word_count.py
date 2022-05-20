str=input()
c=1
for i in range(1,len(str)):
    if str[i].isupper():
        c+=1
print(c)        