import os, random

os.system("clear")

def random_array(n):
    return [random.randint(1, 20) for _ in range(n)]

""" Series20 -> n natural soni va n ta butun son berilgan. Bu sonlar orasidan
o'ng qo'shnisidan kichiklarini va ularning sonini chiqaruvchi programma tuzilsin."""
def func20(n):
    arr = random_array(n)
    print(arr)

    count = 0
    for i in range(n-1):
        if arr[i] < arr[i + 1]:
            print(arr[i])
            count += 1
    print(f"{count} ta.")


""" Series21 -> n natural soni va n ta haqiqiy son berilgan. Bu sonlar o'sish tartibida bo'lsa - true,
aks holda false chiqaruvchi programma tuzilsin."""
def func21(n):
    array = random_array(n)
    arr = list(range(10, 31, 2))

    print(arr, sorted(arr) == arr)
    print(array, sorted(array) == array)


""" Series22 -> n natural soni va n ta haqiqiy son berilgan. Bu sonlar kamayish tartibida bo'lsa - 0,
aks holda qonuniyatni buzgan element nomerini chiqaruvchi programma tuzilsin."""
def func22(n):
    array = random_array(n)
    arr = list(range(9, 31, 3))[::-1]

    if sorted(arr, reverse=True) == arr:
        print(f"{arr} kamayish tartibida: {0}")
    else:
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                print(f"{arr} dagi qonuniyatni buzgan son indeksi {i}")
                break

    if sorted(array) == array:
        print(f"{array} kamayish tartibida: {0}")
    else:
        for i in range(n - 1):
            if array[i] < array[i + 1]:
                print(f"{array} dagi qonuniyatni buzgan son indeks: {i}")
                break


""" Series23 -> n natural soni va n ta haqiqiy son berilgan. Bu sonlar arra shaklida bo'lsa - 0,
aks holda qonuniyatni buzgan element tartib raqamini chiqaruvchi programma tuzilsin.
Agar to'plamning har bir ichki elementi ikkala qo'shnisidan katta yoki kichik bo'lsa,
arra shaklida bo'ladi. Masalan: (2, 3, 1, 5, 4) yoki (5, 3, 4, 2, 6)"""
def func23(n):
    array = random_array(n)
    
    for i in range(1, n - 1):
        if not((array[i] < array[i + 1] and array[i] < array[i - 1]) or (array[i] > array[i + 1] and array[i] > array[i - 1])):
            return print(f"{array} dagi arrasimonlik qonuniyatini buzgan element indeksi: {i}")
    print(f"{array} to'plam arrasimon: {0}")   


""" Series24 -> n natural soni va n ta haqiqiy son berilgan. Bu sonlar orasidan kamida 2 ta nol bor.
Oxirgi 2 ta nol orasidagi sonlar yig'indisini chiqaruvchi programma tuzilsin."""
def func24(arr):
    array = arr[::-1]
    first_zero = array.index(0)
    last_zero = array.index(0, first_zero + 1)
    print(sum(array[first_zero:last_zero]))


""" Series25 -> n natural soni va n ta haqiqiy sonlar berilgan. Bu sonlar orasida kamida 2 ta 0 bor.
Birinchi va oxirgi nol orasidagi sonlar yig'indisini chiqaruvchi programma tuzilsin."""
def func25(arr):
    first_zero = arr.index(0)
    last_zero = -(arr[::-1].index(0) + 1)
    print(sum(arr[first_zero:last_zero]))


""" Series26 -> n, k natural sonlari va n ta haqiqiy son berilgan.
Shu sonlarning k - darajasini chiqaruvchi programma tuzilsin."""
def func26(n, k):
    array = random_array(n)
    arr = list(map(lambda num:num ** k, array))

    print(array)
    print(arr)


""" Series27 -> n natural soni va n ta haqiqiy son berilgan. Birinchi kiritilgan sonning birinchi darajasini,
2-sonning 2-darajasini, n-kiritilgan sonning n-darajasini chiqaruvchi programma tuzilsin."""
def func27(n):
    array = random_array(n)
    print(array)
    for i in range(1, len(array)+1):
        print(array[i-1] ** i)


""" Series28 -> n natural soni n ta haqiqiy son berilgan. Birinchi kiritilgan sonning n-darajasini,
2-kiritilgan sonning (n - 1)-darajasini, n-kiritilgan sonning 1-darajasini chiqaruvchi programma tuzilsin."""
def func28(n):
    array = random_array(n)
    arr = iter(array)
    print(array)
    for i in range(n):
        nxt = next(arr)
        print(f"{nxt} ning {n - i}-darajasi: {nxt ** (n - i)}")


""" Series29 -> n, k natural sonlari va n ta butun sondan iborat k ta to'plam berilgan.
Barcha sonlar yig'indisini chiqaruvchi programma tuzilsin."""
def func29(n, k):
    array = [random_array(n) for _ in range(k)]
    total = sum([sum(arr) for arr in array])
    
    print(array)
    print(f"To'plamdagi barcha sonlar yig'indisi: {total}")