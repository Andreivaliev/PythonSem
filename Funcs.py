def revers_range(num):
    if num > 0:
        revers_range(num-1)
    print(num, end="")


def degree(a,b):
    if b==0:
        return 1
    if b>0:
        return a*degree(a,b-1)
    if b<0: 
        return 1/a*degree(a,b+1) 



   