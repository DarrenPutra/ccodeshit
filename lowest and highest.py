arr = [23, 321, 234, 546, 6, 5467,754, 234, 453, 87]

lowest_num = arr[0]
highest_num = arr[0]

for i in range(len(arr)):
    if arr[i] > highest_num:
        highest_num = arr[i]
    if arr[i] < lowest_num:
        lowest_num = arr[i]
        
print("highest number is : ", highest_num)
print("lowest number is : ", lowest_num)