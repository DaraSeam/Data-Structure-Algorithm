# creating stack
def create_stack():
    stack = []
    return stack

# creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# adding items to the stack
def push(stack, item):
    stack.append(item)
    print("Push item: "+item)

# removing an element from the stack
def pop(stack):
    if(check_empty(stack)):
        return "Stack is empty."
    return stack.pop()


# stack we create:
stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print("Popped item: " +pop(stack))
print("Stack after popping an element: " +str(stack))