import customtkinter as ctk
from tkinter import messagebox
import timeit as t
import random
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(100000)

x = []
def input():
    n = entry.get().strip().split(",") 
    for divideByComma in n:
        divideByComma = divideByComma.strip()
        if divideByComma.isdigit() and int(divideByComma) != 0:
            x.append(int(divideByComma))
        entry.delete(0, 'end')
        showData()

def showData():
    list_label.configure(text=f"Angka yang dimasukkan: {', '.join(map(str, x))}")

def digitPrime1(x):
    dataCopy1 =x[:]
    selectionSort(dataCopy1)
    primes = []
    for num in dataCopy1:
        digit_sum = 0
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        if isPrime(digit_sum):
            primes.append(num)
    return primes

def digitPrime2(x):
    dataCopy2 = x[:]
    insertionSort(dataCopy2)
    primes = []
    for num in dataCopy2:
        digit_sum = 0
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        if isPrime(digit_sum):
            primes.append(num)

def recursiveDigitPrime1(x):
    dataCopy3 = x[:]
    recursiveSelection(dataCopy3,0)
    primes = []
    for num in dataCopy3:
        digit_sum = 0
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        if isPrime(digit_sum):
            primes.append(num)

def recursiveDigitPrime2(x):
    dataCopy4 = x[:]
    recursiveInsertion(dataCopy4,len(dataCopy4))
    primes = []
    for num in dataCopy4:
        digit_sum = 0
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        if isPrime(digit_sum):
            primes.append(num)
   
def isPrime(digit):
    if digit <= 1:
        return False
    for i in range(2, digit-1):
        if digit % i == 0:
            return False
    return True


def selectionSort(arr):
    for i in range(len(arr)):
        temp = i
        for j   in range(i + 1, len(arr)):
            if arr[j] < arr[temp]:
                temp = j
        arr[i], arr[temp] = arr[temp], arr[i]

def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def recursiveSelection(arr,start):
    if start >= len(arr) - 1: 
        return
    else:
        idxMin = findMinIndex(arr, start, start + 1)
        arr[start], arr[idxMin] = arr[idxMin], arr[start]
        recursiveSelection(arr, start + 1)
def findMinIndex(arr, start, current):
    if current >= len(arr):
        return start
    else :
        if arr[current] < arr[start]:
            start = current
        return findMinIndex(arr, start, current + 1)


def recursiveInsertion(arr, n):
    if n <= 1:
        return
    else:
        recursiveInsertion(arr, n - 1) #memanggil diri sendiri
        insert(arr, n - 1) #memanggil function insert
def insert(arr, n):
    if n <= 0 or arr[n] >= arr[n - 1]:
        return
    else:
        arr[n], arr[n - 1] = arr[n - 1], arr[n]
        insert(arr, n - 1)


def deleteData():
    x.clear()
    list_label.configure(text="Belum ada angka yang dimasukkan", font=("Arial", 12))
    label_feedback.configure(text="", font=("Arial", 12))
    label_time1.configure(text="", font=("Arial", 12))
    label_time2.configure(text="", font=("Arial", 12))
    label_time3.configure(text="", font=("Arial", 12))
    label_time4.configure(text="", font=("Arial", 12))

def measureTime():
    excTime1 = t.timeit(lambda: digitPrime1(x), number=1)
    excTime2 = t.timeit(lambda: digitPrime2(x), number=1)
    excTime3 = t.timeit(lambda: recursiveDigitPrime1(x), number=1)
    excTime4 = t.timeit(lambda: recursiveDigitPrime2(x), number=1)
    label_time1.configure(text=f"Dengan iteratif Selection sort program diselesaikan selama:{excTime1:.6f} detik")
    label_time2.configure(text=f"Dengan iteratif Insertion sort program diselesaikan selama:{excTime2:.6f} detik")
    label_time3.configure(text=f"Dengan rekursif Selection sort program diselesaikan selama:{excTime3:.6f} detik")
    label_time4.configure(text=f"Dengan rekursif Insertion sort program diselesaikan selama:{excTime4:.6f} detik")
    Primes = digitPrime1(x)
    if Primes:
        label_feedback.configure(text=f"Bilangan prima dari jumlah digit: {', '.join(map(str, Primes))}")
    else:
        label_feedback.configure(text="Tidak ada bilangan prima ditemukan.")

def compareTime():
    sizes = [10,20,30,40,50,60,70,80,90,100]
    selectionTimes = []
    insertionTimes = []
    recursiveSelectionTimes = []
    recursiveInsertionTimes = []

    for size in sizes:
        data = [random.randint(1, 10000) for _ in range(size)]
        excTime1 = t.timeit(lambda: digitPrime1(data.copy()), number=1)
        selectionTimes.append(excTime1)
        excTime2 = t.timeit(lambda: digitPrime2(data.copy()), number=1)
        insertionTimes.append(excTime2)
        excTime3 = t.timeit(lambda: digitPrime1(data.copy()), number=1)
        recursiveSelectionTimes.append(excTime3)
        excTime4 = t.timeit(lambda: digitPrime2(data.copy()), number=1)
        recursiveInsertionTimes.append(excTime4)
    plot_graph(sizes, selectionTimes, insertionTimes,recursiveSelectionTimes,recursiveInsertionTimes)

def plot_graph(sizes, selectionTimes, insertionTimes,recursiveSelection,recursiveInsertion):
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, selectionTimes, label='Selection Sort', marker='o')
    plt.plot(sizes, insertionTimes, label='Insertion Sort', marker='o')
    plt.plot(sizes, recursiveSelection, label='Recursive Selection Sort', marker='o')
    plt.plot(sizes, recursiveInsertion, label='Recursive Insertion Sort', marker='o')
    plt.title('Execution Time Comparison: Selection Sort vs Insertion Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid()
    plt.show()


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")  

# Membuat window
window = ctk.CTk()
window.title("Tubes AKA")
#window.iconbitmap(r"C:\Users\hp\OneDrive - Telkom University\Coolyeah\Semester 3\Tugas\Analisis Kompleksitas Algoritma\chart_finance_office_strategy_business_study_management_icon_263044.ico")
window.geometry("600x400")

label = ctk.CTkLabel(window, text="Did it prime?", font=("Bookman Old Style", 40))
label.pack(pady=10)

#label_Descriptions = ctk.CTkLabel(window, text="Aplikasi ini akan memeriksa bilangan mana saja yang memiliki penjumlahan digit prima",font=("Arial", 12))
#label_Descriptions.pack(pady=2)
#label_Descriptions2 = ctk.CTkLabel(window, text="(Misal: angka 12 merupakan prima karena 1+2 =3, 3 adalah bilangan prima)",font=("Arial", 12))
#label_Descriptions2.pack(pady=1)

entry = ctk.CTkEntry(window, width=200)
entry.pack(pady=10)

#label_note = ctk.CTkLabel(window, text="Note : Gunakan tanda koma (',') untuk memisahkan input.", font=("Arial",12),text_color="red")
#label_note.pack(pady = 0.1)

#label_note2 = ctk.CTkLabel(window, text="Input selain angka tidak akan masuk datar", font=("Arial",12),text_color="red")
#label_note2.pack(pady = 0.1)

button_frame = ctk.CTkFrame(window,fg_color=None)
button_frame.pack(pady=10)

button_tambah = ctk.CTkButton(button_frame, text="Tambah angka", command=input)
button_tambah.pack(side="left", padx=10)

button_hapus = ctk.CTkButton(button_frame, text="Hapus Data", command=deleteData)
button_hapus.pack(side="left", padx=10)

button_frame2 = ctk.CTkFrame(window,fg_color=None)
button_frame2.pack(pady=10)

button_prima = ctk.CTkButton(button_frame2, text="Cari Prima", command=measureTime)
button_prima.pack(side = "left",padx=10)

button_graph = ctk.CTkButton(button_frame2, text="Tampilkan grafik", command=compareTime)
button_graph.pack(side = "left",padx=10)

list_label = ctk.CTkLabel(window, text="", font=("Arial", 12))
list_label.pack(pady=10)

label_feedback = ctk.CTkLabel(window, text="", font=("Arial", 12))
label_feedback.pack(pady=5)

label_time1 = ctk.CTkLabel(window,text="",font=("Arial", 12))
label_time1.pack(pady=5)
label_time2 = ctk.CTkLabel(window,text="",font=("Arial", 12))
label_time2.pack(pady=5)
label_time3 = ctk.CTkLabel(window,text="",font=("Arial", 12))
label_time3.pack(pady=5)
label_time4 = ctk.CTkLabel(window,text="",font=("Arial", 12))
label_time4.pack(pady=5)

window.mainloop()


