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

# s=int(input("Введите общее количество журавликов(число кратное 6) :"))

# if s%6==0:
#     print("Петя - {}; Катя - {}; Серёжа - {};".format(s//6,2*s//3,s//6))
# else:
#     print("Некорректное значение для данной задачи")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

k = int(input("Введите шестизначное число: "))

if k > 99999 and k < 1000000:
    if k//100000+k//10000%10+k//1000%10==k//100%10+k//10%10+k%10 :
        print("Yes")
    else :
        print("No")
else :
    ("Число не является шестизначным")