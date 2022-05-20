def sum_digits(string):
    sum=0
    for i in string:
        if i.isdigit()==True:
            sum+=int(i)
    return sum
string=input()
print(sum_digits(string))