# Stack
# push = add
# pop = remove the last element
# peek = point to the last element
# isEmpty= check stack have element or not
# size = check how many element in stack
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    # Create a stack
mystack=Stack()
mystack.push("A")
mystack.push("B")
mystack.push("C")
print("Stack: ",mystack.stack)

print("Pop: ",mystack.pop())



# Queue 
# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,element):
#         self.queue.append(element)
#     def dequeue(self):
#         if self.isEmpty():
#             return "The queue is empty"
#         return self.queue.pop(0)
#     def isEmpty(self):
#         return len(self.queue)==0
#     def peek(self):
#         if self.isEmpty():
#             return "The queue is empty"
#         return self.queue[0]
#     def size(self):
#         return len(self.queue)
# obj=Queue()
# obj.enqueue("A")
# obj.enqueue("B")
# obj.enqueue("C")
# print(obj.queue)
# print(obj.dequeue())
# print(obj.size())

# # Queue in class
# myqueue=[]
# # Enqueue
# myqueue.append("A")
# myqueue.append("B")
# myqueue.append("C")
# print("Queue:",myqueue)
# # Dequeue
# dequeue=myqueue.pop(0)
# print("Dequeue:",myqueue)
# # Peek
# peek=myqueue[0]
# print("Peek:",peek)
# # IsEmpty
# IsEmpty=bool(myqueue)
# print(IsEmpty)
# # Size 
# size=len(myqueue)
# print("Size:",size)