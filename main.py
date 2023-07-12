import matplotlib.pyplot as plt
import numpy as np

lst = np.random.randint(1, 100, 50)
x = np.arange(0, 50, 1)

#bubble Sort
def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            plt.bar(x, lst)
            plt.pause(0.0001)
            plt.clf()
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    plt.show()

#gnome Sort
def gnomeSort(lst):
    index = 0
    while index < len(lst):
        if index == 0:
            index = index + 1
        if lst[index] >= lst[index - 1]:
            index = index + 1
        else:
            lst[index], lst[index - 1] = lst[index - 1], lst[index]
            index = index - 1
        plt.bar(x, lst)
        plt.pause(0.0001)
        plt.clf()
    return lst

#insertion Sort
def insertionSort(lst):
    if (n := len(lst)) <= 1: return
    for i in range(1, n):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            plt.bar(x, lst)
            plt.pause(0.0001)
            plt.clf()
        lst[j + 1] = key

    return lst

#cockail Sort
def cocktailSort(lst):
    n = len(lst)
    swapped, start, end = True, 0, n - 1

    while (swapped == True):
        swapped = False

        for i in range(start, end):
            if (lst[i] > lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
            plt.bar(x, lst)
            plt.pause(0.0001)
            plt.clf()

        if (swapped == False): break

        swapped, end = False, end - 1

        for i in range(end - 1, start - 1, -1):
            if (lst[i] > lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
            plt.bar(x, lst)
            plt.pause(0.0001)
            plt.clf()

        start = start + 1

    return lst



def heapify(lst, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lst[i] < lst[l]:largest = l
    if r < n and lst[largest] < lst[r]: largest = r

    if largest != i:
        (lst[i], lst[largest]) = (lst[largest], lst[i])
        heapify(lst, n, largest)
#heap Sort
def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        plt.bar(x, lst)
        plt.pause(0.0001)
        plt.clf()

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)
        plt.bar(x, lst)
        plt.pause(0.0001)
        plt.clf()



def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
        plt.bar(x, lst)
        plt.pause(0.001)
        plt.clf()

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
#quick Sort
def quickSort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quickSort(lst, low, pi - 1)
        quickSort(lst, pi + 1, high)
        plt.bar(x, lst)
        plt.pause(0.001)
        plt.clf()

#selection Sort
def selectionSort(lst):
    for ind in range(len(lst)):
        min_index = ind

        for j in range(ind + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        plt.bar(x, lst)
        plt.pause(0.001)
        plt.clf()
        (lst[ind], lst[min_index]) = (lst[min_index], lst[ind])


selectionSort(lst)
