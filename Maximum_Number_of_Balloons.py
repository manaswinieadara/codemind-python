text=input()
bcount=0
acount=0
lcount=0
ocount=0
ncount=0
for ch in text:
    if ch=="b":
        bcount+=1
    elif ch=="a":
        acount+=1
    elif ch=="l":
        lcount+=1
    elif ch=="o":
        ocount+=1
    elif ch=="n":
        ncount+=1
print(min(bcount,acount,lcount//2,ocount//2,ncount))        
         