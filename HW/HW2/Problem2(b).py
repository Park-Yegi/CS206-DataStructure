
# the form of input(item) is tuple(data, priority)
# Let small number has high priority
# index 0 is front of queue

# Make Priority Queue class
class PriorityQueue(object):
    # Create Priority Queue
    def __init__(self, max_pq_size):
        self.pq = []
        self.max_pq_size = max_pq_size
        self.rear = -1

    # Function IsFull
    def IsFull(self):
        if self.rear >= self.max_pq_size - 1:
            return True
        else:
            return False

    # Function IsEmpty
    def IsEmpty(self):
        if self.rear < 0:
            return True
        else:
            return False

    # Function Top
    def Top(self):
        if self.IsEmpty():
            return "Priority Queue is empty, don't have top element"
        else:
            return self.pq[0]

    # Function Pop
    def Pop(self):
        if self.IsEmpty():
            return "Priority Queue is empty, cannot pop element"
        else:
            pop = self.pq[0]
            self.pq = self.pq[1:]
            self.rear -= 1
            return pop

    # Function Push
    def Push(self, item):
        item_list = [item]
        if self.IsFull():
            return "Priority Queue is full, cannot add element"
        else:
            if self.rear < 0:
                self.pq = item_list
                self.rear += 1
            else:
                for i in range(len(self.pq)):
                    if item[1] < self.pq[i][1]:
                        front_list = self.pq[:i]
                        rear_list = self.pq[i:]
                        self.pq = front_list + item_list + rear_list
                        self.rear += 1
                        break
                    elif i == len(self.pq)-1:
                        self.pq += item_list
                        self.rear += 1
                    else:
                        pass
        return self.pq
