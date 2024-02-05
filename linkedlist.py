max_size = 6
datalist = [None for i in range(max_size)]
pointerlist=[0 for i in range(max_size)]


for i in range (max_size):
    pointerlist[i] = i + 1
pointerlist[max_size-1] = -1
 
sp = -1
hp = 0


def isfull():
    global hp
    if hp == -1:
        return True
    else:
        return False


def isempty():
    global sp
    if sp == -1:
        return True
    else:
        return False
    
def insert(val):
    global sp
    global hp
    if  isfull():
        print("linked list full")
    else:
        tempsp = sp
        sp = hp
        datalist[sp] = val
        hp = pointerlist[hp]
        pointerlist[sp] = tempsp


def delete(val):
    global sp
    global hp
    index = sp
    oldindex = sp
    while datalist[index] != val and index != -1:
        oldindex = index
        index = pointerlist[index]
        print(index)  
    if index == -1:
        print("search element does not exist")
    else:
        if index == sp:
            sp = pointerlist[sp]
        datalist[index] = None
        pointerlist[oldindex] = pointerlist[index]
        pointerlist[index] = hp
        hp = index

insert(10)
print(datalist, pointerlist)  
insert(20)
print(datalist, pointerlist)   
insert(30)
print(datalist, pointerlist)   
insert(40)
print(datalist, pointerlist)   
insert(50)
print(datalist, pointerlist)   
insert(60)
print(datalist, pointerlist)   
delete(60)
print(datalist, pointerlist)
delete(50)
print(datalist, pointerlist)
delete(40)
print(datalist,pointerlist)


    






    


