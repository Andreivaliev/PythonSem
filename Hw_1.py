# Задача 2: Найдите сумму цифр трехзначного числа.

# a=int(input("Введите трёхзначное число: "))

# if a > 99 and a < 1000 :
#     print(a//100 + a//10%10+a%10)
# else:
#     print("Введено не трёхзначное число")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

s=int(input("Введите общее количество журавликов(число кратное 6) :"))

if s%6==0:
    print("Петя - {}; Катя - {}; Серёжа - {};".format(s//6,2*s//3,s//6))
else:
    print("Некорректное значение для данной задачи")
