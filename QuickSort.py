# QuickSort Python
#Rafael & Fellipe

#Transformar "QuickSort.txt" em um Array []
f = open("QuickSort.txt", "r")
intarray = []
for line in f:
    intarray.append(int(line))
f.close()

#Pivot == Primeiro Elemento

def partition_first(array, leftend, rightend):
    pivot = array[leftend]
    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1 

#Quick Sort Pivot == 1 Elemento
def quick_sort1(array, leftindex, rightindex):
    global firstcomparison
    if leftindex < rightindex:
        
        newpivotindex = partition_first(array, leftindex, rightindex)
        
        firstcomparison += (rightindex - leftindex - 1)
        
        quick_sort1(array, leftindex, newpivotindex) 
        
        quick_sort1(array, newpivotindex + 1, rightindex)
        

#Pivot == Ultimo Elemento
def partition_last(array, leftend, rightend):
    
    pivot = array[rightend-1]

    array[rightend-1] = array[leftend]
    array[leftend] = pivot
    
    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1 

#Quick Sort Com o Pivot == Ultimo Elemento
def quicksort_last(array, leftindex, rightindex):
    global lastcomparison
    if leftindex < rightindex:

        newpivotindex = partition_last(array, leftindex, rightindex)

        lastcomparison += (rightindex - leftindex - 1)

        quicksort_last(array, leftindex, newpivotindex)
        quicksort_last(array, newpivotindex + 1, rightindex)




#Pivot == Mediana
def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c

def partition_median(array, leftend, rightend):
    left = array[leftend]
    right = array[rightend-1]
    length = rightend - leftend
    if length % 2 == 0:
        middle = array[leftend + length/2 - 1]
    else:
        middle = array[leftend + length/2]
  
    

    pivot = median(left, right, middle)

    pivotindex = array.index(pivot) #only works if all values in array unique

    array[pivotindex] = array[leftend]
    array[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1 

#QuickSort Tendo o Pivot == Mediana
def quicksort_median(array, leftindex, rightindex):
     global mediancomparison
     if leftindex < rightindex:

         newpivotindex = partition_median(array, leftindex, rightindex)

         mediancomparison += (rightindex - leftindex - 1)
         quicksort_median(array, leftindex, newpivotindex)
         

         quicksort_median(array, newpivotindex + 1, rightindex)

