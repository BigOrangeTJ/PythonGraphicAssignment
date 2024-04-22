# Richard Partridge
# Queue in Python

class PriorityQueue:
    def __init__(self):
        self.p_queue = []

    def enqueue(self, item):
        self.p_queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.p_queue.pop(0)

    def is_empty(self):
        return len(self.p_queue) == 0


def apply_wfq(queues):
    while True:
        if not any(queue.is_empty() for queue in queues):
            if queues[0].is_empty():
                queues.pop(0)
            else:
                print(queues[0].dequeue())
        else:
            break


def print_prioritized_queues(queues):
    for queue in queues:
        while not queue.is_empty():
            print(queue.dequeue())


def main():
    # Initialize queues
    premium_queue = PriorityQueue()
    standard_queue = PriorityQueue()
    economy_queue = PriorityQueue()

    # Read data from input file
    with open('input queue-1.txt', 'r') as f:
        data = f.readlines()

    # Parse data and enqueue into appropriate queues
    for line in data:
        priority = line[0]
        packet = line[2:].strip()
        if priority == 'P':
            premium_queue.enqueue(packet)
        elif priority == 'S':
            standard_queue.enqueue(packet)
        elif priority == 'E':
            economy_queue.enqueue(packet)

    # Print prioritized queues
    print("Premium Queue:")
    print_prioritized_queues([premium_queue])

    print("Standard Queue:")
    print_prioritized_queues([standard_queue])

    print("Economy Queue:")
    print_prioritized_queues([economy_queue])


if __name__ == "__main__":
    main()
