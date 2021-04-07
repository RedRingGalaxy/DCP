# Problem Statement [Easy]
'''
Implemet a stack API only using Heap.
'''

class HeapNode:
    def __init__(self,data,position) -> None:
        self.data = data
        self.position = position

    def __lt__(self,other):
        return self.position < other.position

class Heap:
    def __init__(self) -> None:
        self.__heap = []
        self.count = 0

    def size(self) -> int:
        return len(self.__heap)

    def printHeap(self):
        for i in self.__heap:
            print(i.data, i.position)

    def push(self,data) -> None:
        node = HeapNode(data, self.count)
        if self.size() == 0:
            self.__heap.append(node)
            self.count += 1
        else:
            self.__heap.append(node)
            self.count += 1
            for i in range((self.size()//2)-1,-1,-1):
                self.heapify(i)

    def pop(self) -> int:

        if self.size() == 0:
            return None

        self.__heap[0] , self.__heap[self.size()-1] = self.__heap[self.size()-1], self.__heap[0]

        poped = self.__heap.pop()
        self.count -= 1

        for i in range((self.size()//2)-1,-1,-1):
            self.heapify(i)

        return poped.data

    def heapify(self,i) -> None:
        large = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left <= self.size() -1 and self.__heap[large] < self.__heap[left]:
            large = left

        if right <= self.size() -1 and self.__heap[large] < self.__heap[right]:
            large = right

        if large != i:
            self.__heap[i] , self.__heap[large] = self.__heap[large], self.__heap[i]
            #self.heapify(large)

if __name__ == "__main__":
    h = Heap()
    h.push(1)
    h.push(2)
    h.push(9)
    h.push(4)
    h.push(2)
    h.push(10)
    #h.printHeap()
    for i in range(h.size()):
       print(h.pop())
