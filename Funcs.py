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

def find_farthest_orbit(orbits):
    list1=list(filter(lambda x: x[0]!=x[1],orbits))
    max=0
    count=0
    list2=[]
    for i in list1:
        if i[0]*i[1]>max:
            max=i[0]*i[1]
            count+=1
            list2.append((i[0],i[1]))
            if count>1:
                list2.pop(0)
    return list2
