# Задача №31
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1= 1, ak= ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1)+fib(n-2)
# n=int(input("Введите номер числа Фибоначчи: "))
# print(fib(n))

# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

def rev(arg):
    max=1
    new=[]
    for i in arg:
        k=int(i)
        if k>max:
            max=k
    for i in arg:
        k=int(i)
        if k==max:
            k=1
        new.append(k)
        print(max)
        print(k)
    return new


arg=[]
r=0
while r<6:
    r=int(input("Введите число: "))
    arg.append(r)
    if r==6:
        arg.pop()
print(rev(arg))