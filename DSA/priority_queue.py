
class PriorityQueue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join(str(i) for i in self.queue)

    def is_Empty(self):
        return len(self.queue) == 0

    # adding to queue
    def insert(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"

        max_i = 0
        for i in range(len(self.queue)):
            if self.queue[i] >= self.queue[max_i]:
                max_i = i
        large = self.queue[max_i]
        del self.queue[max_i]
        return large


if __name__ == "__main__":
    my_queue = PriorityQueue()
    my_queue.insert(11)
    my_queue.insert(21)
    my_queue.insert(3)
    my_queue.insert(2)
    my_queue.insert(5)

    print(my_queue)

    while not my_queue.is_Empty():
        print(my_queue.dequeue())