def parent(i): return (i-1)//2;
def left(i): return i*2 +1;
def right(i): return i*2 +2;

def bubble_down(arr ,i , n):

    # max up
    maxi = i

    l = left(i)
    r = right(i)

    if l < n and arr[l] > arr[maxi]:
        maxi = l
    if r < n and arr[r] > arr[maxi]:
        maxi = r

    if maxi != i :
        arr[i] , arr[maxi] = arr[maxi] ,arr[i]
        bubble_down(arr, maxi , n)


def buildHeap(arr):
    n = len(arr)
    for i in range(n-1 , -1,-1):
        bubble_down(arr , i , n)

def heapSort(arr):
    buildHeap(arr)

    n = len(arr)

    for i in range(n-1):

        arr[0], arr[n-i-1] =  arr[n-i-1] ,arr[0]

        bubble_down(arr ,0,n -i -1  )


arr = [123,22,13,15,64,32]
heapSort(arr)
print(arr)
