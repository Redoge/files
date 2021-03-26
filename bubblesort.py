import time
from random import randint
import re
errCode = 0
def bubbleSort(arr):
    start_time = time.time() 
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print((time.time() - start_time))

lenght = input('Введіть розмір масиву, або сам масив:  ')
count = len(re.findall(r'\b\d+\b', lenght)) #Кількість чисел
if count != 1:
    arr = list(map(int, lenght.split())) 
else:
    lenght = int(lenght)
    types = int(input("Введіть номер складності: 0, 1 або 2 => "))
    arr = []
    if types == 0:
        k = 0
        while k < lenght:
            arr.append(k)
            k += 1
    elif types == 1:
        k = 0
        while k < lenght:
            arr.append(randint(1, lenght))
            k += 1
    elif types == 2:
        k = lenght
        while k > 0:
            arr.append(k)
            k -= 1
    else:
        print("Складність введено не вірно!!!")
        errCode = 1

if errCode == 1:
    print(f"Error {errCode} ")
else:
    bubbleSort(arr)
    endans = int(input('Вивести впорядкований масив? 0 - Ні, 1 - Так:  '))
    if endans == 1: 
        print ("Впорядкований масив:")
        ans = ""
        for i in range(len(arr)):
            ans = str(ans) + str(arr[i]) + " "     
        print(ans)
    elif endans == 0:
        print("Кінець програми---:)")
    else:
        errCode = 2
        print(f"Error {errCode}\nКінець програми---;)")
