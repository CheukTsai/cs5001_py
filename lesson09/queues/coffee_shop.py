# from queue_linked_list import Queue
from queue_python_list import Queue

coffee_queue = Queue()

while True:
    to_do = input("What do you want to do?\n")
    if (to_do) == "order":
        name = input("What's your name?\n")
        coffee_queue.enqueue(name)
    elif to_do == "collect":
        if not coffee_queue.is_empty():
            print("Coffee is ready for", coffee_queue.dequeue())
        else:
            print("No more orders coming")
    elif to_do == "check queue":
        print(coffee_queue)
