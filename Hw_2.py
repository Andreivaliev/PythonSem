# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# n=int(input("Общее количество монет: "))
# r=range(n)
# count1=0
# count2=0
# for i in r:
#     pos=int(input("Ведите число 1, если монета лежит вверх решкой; 0, если гербом :"))
#     if pos==0:
#         count1+=1
#     else:
#         count2+=1
# if count1>count2:
#     print(count2)
# else:
#     print(count1)