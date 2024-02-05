max_size = 6
lQueue = [None for i in range(max_size)]
front = 0
rear = -1

def isfull():
    if rear + 1 == max_size:
        return True
    else:
        return False

def isempty():
    if front > rear:
        return True
    else:
        return False
    
def enqueue(value):
    global rear
    if isfull() == True:
        print ("Queue full cannot enqueue value")
    else:
        rear += 1
        lQueue[rear] = value

def dequeue():
    global front
    if isempty() == True:
        print("Queue is empty cannot dequeue item")
    else:
        item = lQueue[front]
        lQueue[front] = None
        front += 1
        return item

print(isfull())
print(isempty())
enqueue(1)
print(lQueue)
enqueue(1)
print(lQueue)
enqueue(1)
print(lQueue)
enqueue(1)
print(lQueue)
enqueue(1)
print(lQueue)
enqueue(1)
print(lQueue)
enqueue(1)
print(lQueue)
dequeue()
print(lQueue)
dequeue()
print(lQueue)
dequeue()
print(lQueue)
dequeue()
print(lQueue)
dequeue()
print(lQueue)
dequeue()
print(lQueue)
dequeue()
print(lQueue)
