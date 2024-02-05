# arr = [9, 4, 5, 6, 5, 7, 4, 3]
# temp = 0
# for Pass in range(len(arr-1)):
#     for i in range(len(arr-1)):
#         if arr[i] > arr[i+1]:
#             temp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = temp
# print(arr)

arr = [9, 4, 5, 6, 5, 7, 4, 3]
temp= 0
count = 0
swap = True
while swap == True and count <= (len(arr)-1):
    swap = False
    for i in range (len(arr)-1-count):
        if arr[i] > arr[i+1]:
             temp = arr[i]
             arr[i] = arr[i+1]
             arr[i+1] = temp
             swap = True
    count += 1
print(arr)
