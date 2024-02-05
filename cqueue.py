max_size = 6
lQueue = [None for i in range(max_size)]
front = -1
rear = -1

def isempty():
    if front == -1 and rear==-1:
        return True
    else:
        return False
    
def  isfull():
    if (rear + 1) % max_size  == front:
        return True
    else:
        return False

def enqueue(value):
    global rear
    global front
    if isfull():
        print("Queue Full cannot enqueue value")
    else:
        if isempty():
            front = 0
        rear = (rear + 1) % max_size
        lQueue[rear] = value
        

def dequeue():
    global front, rear
    if isempty():
        print("Queue empty cannot dequeue")
    else:
        item = lQueue[front]
        lQueue[front] = None
        if front == rear:
            front = -1
            rear = -1
        else:
            front = (front + 1) % max_size
        return item
    
    
for i in range(6):
    enqueue(1)
    print(lQueue)

for i in range(7):    
    dequeue()
    print(lQueue)

