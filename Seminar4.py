# Задача №27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# text=input("Введите текст: ")
# myList=text.split()
# v=tuple(myList)
# k = len(v)
# print(k)


# Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# text=input("Введите текст: ")
# myList=text.split()
# dictionary={}
# count=""
# for letters in myList:
#     if letters in dictionary.keys():
#         dictionary[letters]+=1
#         count += f"{letters}_{dictionary[letters]}"+" "
#     else:
#         dictionary[letters]=0
#         count += letters+" "
# print(count)