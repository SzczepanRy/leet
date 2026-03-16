

def merge(l,r):

    result=[]
    i = j = 0

    while i < len(l) and j < len(r):
        if r[j]<=l[i]:
            result.append(r[j])
            j+=1
        else:
            result.append(l[i])
            i+=1


    result.extend(l[i:])
    result.extend(r[j:])
    return result



def mergeSort(arr):

    if len(arr)<=1:
        return arr

    n = len(arr)
    mid = n//2

    l = arr[:mid]
    r = arr[mid:]

    sl = mergeSort(l)
    sr = mergeSort(r)

    return merge(sl,sr)

arr = [12,21,2,3,3,3,1,2,1,1,11,1]
sort = mergeSort(arr)
print(sort)


def fancym(A,B,p,q,r):

    i = p
    j = q
    k = p

    while i < q and j < r:

        if A[i] <= A[j]:
            B[k] = A[i]
            i+=1

        else:
            B[k] = A[j]
            j+=1

        k+=1


    while i < q :
        B[k] = A[i]
        i+=1
        k+=1

    while j < r :
        B[k] = A[j]
        j+=1
        k+=1


    for t in range(p,r):
        A[t] = B[t]

def fancysort(A,B , p , r):

    if r-p >1:
        q = (p+r)//2

        fancysort(A,B,p,q)
        fancysort(A,B,q,r)
        fancym(A,B,p,q,r)


A=[12,213,4,23,1,43,23]

n = len(A)
B = [0]*n
fancysort(A,B,0,n)
print(A,B)





