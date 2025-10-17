import random

def generateList(elementNum):
    for i in range(elementNum):
        return [i for i in range(elementNum)]
    return lst

def shuffle(lst): # performs Fisher-Yates Shuffle
    for i in range(len(lst)-1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst
    

def bogo(lst):
    sortedList = sorted(lst)
    isSorted = False
    attempts = 0
    while isSorted == False:
        lst = shuffle(lst)
        attempts += 1
        print(f"Attempt: {attempts}; {lst}")
        if lst == sortedList:
            isSorted = True

def quick(lst):
    length = len(lst)
    if length <= 1:
        return lst
    pivot = lst.pop()
    high = []
    low = []
    for i in lst:
        if i > pivot:
            high.append(i)
        else:
            low.append(i)
    return quick(low) + [pivot] + quick(high)
    
#def selection(lst):

#def merge(lst):

def insertion(lst):
    passes = 0
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        passes += 1
        print(f"Passes: {passes}; {lst}")
    
def bubble(lst, elementNum):
    swaps = 0
    for i in range(elementNum):
        for j in range(0, elementNum-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swaps += 1
                print(f"Swap: {swaps}; {lst}")


print("Enter number of elements:")
elementNum = int(input())
lst = generateList(elementNum)
print(f"Sorted List: {lst}")
shuffle(lst)
print(f"Shuffled list: {lst}")
lst = quick(lst)
print(f"Quick Sorted List: {lst}")
print("List sorted!")
