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
    pass


""" Series23 -> n natural soni va n ta haqiqiy son berilgan. Bu sonlar arra shaklida bo'lsa - 0,
aks holda qonuniyatni buzgan element tartib raqamini chiqaruvchi programma tuzilsin.
Agar to'plamning har bir ichki elementi ikkala qo'shnisidan katta yoki kichik bo'lsa,
arra shaklida bo'ladi. Masalan: (2, 3, 1, 5, 4) yoki (5, 3, 4, 2, 6)"""
def func23(n):
    pass


""" Series24 -> n natural soni va n ta haqiqiy son berilgan. Bu sonlar orasidan kamida 2 ta nol bor.
Oxirgi 2 ta nol orasidagi sonlar yig'indisini chiqaruvchi programma tuzilsin."""
def func24(n):
    pass


""" Series25 -> n natural soni va n ta haqiqiy sonlar berilgan. Bu sonlar orasida kamida 2 ta 0 bor.
Birinchi va oxirgi nol orasidagi sonlar yig'indisini chiqaruvchi programma tuzilsin."""
def func25(n):
    pass


""" Series26 -> n, k natural sonlari va n ta haqiqiy son berilgan.
Shu sonlarning k - darajasini chiqaruvchi programma tuzilsin."""
def func26(n, k):
    pass


""" Series27 -> n natural soni va n ta haqiqiy son berilgan. Birinchi kiritilgan sonning birinchi darajasini,
2-sonning 2-darajasini, n-kiritilgan sonning n-darajasini chiqaruvchi programma tuzilsin."""
def func27(n):
    pass


""" Series28 -> n natural soni n ta haqiqiy son berilgan. Birinchi kiritilgan sonning n-darajasini,
2-kiritilgan sonning (n - 1)-darajasini, n-kiritilgan sonning 1-darajasini chiqaruvchi programma tuzilsin."""
def func28(n):
    pass


""" Series29 -> n, k natural sonlari va n ta butun sondan iborat k ta to'plam berilgan.
Barcha sonlar yig'indisini chiqaruvchi programma tuzilsin."""
def func29(n, k):
    pass