from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.popleft()
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        """View the front item without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front item:", q.peek())
    q.dequeue()
    print("Queue size:", q.size())
    q.dequeue()
    q.dequeue()
    q.dequeue()  # Trying to dequeue from empty queue