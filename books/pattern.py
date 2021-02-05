n=int(input())
space=n-1
star=1

for i in range(n):
    for j in range(space):
        print("\t",end="")
        for k in range(star):
            print("*\t",end="")
    space=space-1
    star=star+1
    print()