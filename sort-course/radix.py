
def count_srt(arr , place ):
    counts = [0]*10
    for el in arr:
        dig = (el//place)%10
        counts[dig] +=1

    ## wodomagic illogical
    ind = 0
    for i , count in enumerate(counts):
        counts[i] = ind
        ind +=count

    sorted = [0]*len(arr)


    for num in arr:
        dig = (num//place)%10
        sorted[counts[dig]] = num
        counts[dig]+=1
    arr[:] = sorted[:]

def radix(arr):

    shift = min(arr)

    arr[:] = [num - shift for num in arr]

    maxel = max(arr)

    place = 1
    while place <= maxel:
        count_srt(arr,place)
        place *=10

    arr[:] = [num + shift for num in arr]




arr=[32,41,412,421,1543,213,321,213]
radix(arr)

print(arr)
