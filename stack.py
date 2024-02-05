max_size = 6 #max_size is a constant
stack = [None for i in range (max_size)]
top = -1 #top is an integer

print(stack)

def isfull():
    if top == max_size-1:
        return True
    else:
        return False

def isempty():
    if top == -1:
        return True
    else:
        return False    

def push(value):
    global top
    if isfull() == True:
        print("Stack Full can't push item into the stack")
    else:
        top += 1
        stack[top] = value
    
def pop():
    global top
    if isempty() == True:
        print("Stack is empty cannot pop")
    else:
        item = stack[top]
        stack[top] = None
        top = top-1
        return item
    
def peek():
    return stack[top]


push(6)
print(stack)
push(7)
print(stack)
push(4)
print(stack)
push(8)
print(stack)
push(0)
print(stack)
push(2)
print(stack)
push(9)
print(stack)

pop()
print(stack)

pop()
print(stack)

pop()
print(stack)

pop()
print(stack)

pop()
print(stack)

pop()
print(stack)

pop()
print(stack)

print(peek())
