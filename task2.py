#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#from random import randint
#num = int(input('Введите размер списка '))
#list = []
#list2 = []
#for i in range(num):
#    list.append(randint(0, 9))
#list2 = list.copy()
#list2.reverse()
#result = []
#for i in range(len(list)):
#    result.append(list[i] * list2[i])
#print(list)
#print(list2)
#print(result)


from random import randint


number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)

