#Problem Statement [Medium]
'''
Implement a queue using Two Statcks. Recall that queue is a FIFO DS with the following methods:
1.Enqueue, which insert an element into queue
2.Dequeuq, which remove an element from the queue
'''

# Implement a Queue usign two stacks
# Here we consider list as stack
class Stacked_Queue:
    
    def __init__(self):
        self._stack1 = list()
        self._stack2 = list()

    # Enqueue append the value into the stack1
    def enqueue(self,value):
        self._stack1.append(value)

    # Dequeue pop all items except last one from statk1 and append it to stack2
    # pop last item from stack1 and store it to the local variable for return 
    # Pop all items from stack2 and append it to stack1
    def dequeue(self):
        for i in range(len(self._stack1)-1):
            self._stack2.append(self._stack1.pop())
        
        pop_itm = self._stack1.pop()

        for i in range(len(self._stack2)):
            self._stack1.append(self._stack2.pop())

        return pop_itm

if __name__ == "__main__":
    q1 = Stacked_Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)

    print(q1.dequeue(),q1.dequeue(),q1.dequeue())
