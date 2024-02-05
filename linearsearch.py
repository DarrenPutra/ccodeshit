arr = [23, 321, 234, 546, 6, 5467,754, 234, 453, 87]
count = 0
x = 0
found = False
search = int(input("Input your search element: "))
# for i in range(len(arr)):
#     if arr[i] == search:
#         found = True
while found != True and count <= (len(arr)-1):
    if arr[count-1] == search:
        found = True 
    count += 1

if found:
    print("found")
else:
    print("not found")


