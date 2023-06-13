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


def sum(a,b):

    if a==0:
        return b
    return sum(a-1,b+1)


def sum_of_dividers(num):
    sum=1
    for i in range(2, num // 2 + 1):
        if num %i == 0:
            sum+=i
    return sum


