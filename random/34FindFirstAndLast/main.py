
arr =[2,3,1,21,3,3,54]
target= 21
min=9999
max = -1

print(arr)
def sort(arr , min ,max, gap, target):
    splitI = len(arr)//2
    left= arr[0:splitI]
    right= arr[splitI:len(arr)]
    if( len(left) >0 and len(right) >0):
        min, max= sort(arr[0:splitI] ,min,max, gap,target  )
        min ,max = sort(arr[splitI:len(arr)] ,min, max, gap + splitI, target)

    if(arr[0] == target):
        if(gap < min):
            min = gap
        if(gap > max):
            max = gap
        print( gap )

    return min ,max


min , max = sort(arr , min, max,0 ,target)
print(min,max)
