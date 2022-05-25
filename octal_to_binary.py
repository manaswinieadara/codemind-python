def OctToBin(o):
    return bin(int(o,8))

print(end="")
onum=input()


bnum=OctToBin(onum)
print(bnum[2:])