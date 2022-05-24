n=int(input())
c=1
x=1
while x*x<=n:
    if n==x*x:
        print("True")
        c=0
        break
    x+=1
if(c!=0):
    print("False")
    
    