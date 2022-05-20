test_cases=int(input())
for i in range(test_cases):
    count=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        rem=i%10
        if rem==2 or rem ==3 or rem==9:
            count+=1
    print(count)        
        