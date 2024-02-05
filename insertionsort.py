arr = [9, 4, 5, 6, 15 , 7, 57, 3, 8]
for i in range (len(arr)):
    value = arr[i]
    j = i 
    print(arr)
    while j > 0 and arr[j-1] > value:
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = value
print(arr)
    