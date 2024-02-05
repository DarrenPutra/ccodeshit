arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low = 0
high = len(arr)-1


# def binsearch():
#     low = 0
#     high = len(arr) - 1
#     found = False
#     se = int(input("input your search element: "))
#     while (found == False ) and (low <= high):
#         mid = int((high + low) / 2 )
#         if arr[mid] == se:
#             found = True
#         elif arr[mid] > se:
#             high = mid - 1                                                            
#         elif arr[mid] < se:
#             low = mid + 1
#     if found:
#         print("found")
#     else:
#         print("not found")

def bsearch(arr, high, low, se):
    mid = int((high + low)/2)
    if se not in arr:
        return("Not found")
    if arr[mid] == se:
        return mid
    elif arr[mid] > se:
        high = mid-1
    elif arr[mid] < se:
        low = mid + 1
    return bsearch(arr, high, low, se)
print(bsearch(arr,high,low,11))