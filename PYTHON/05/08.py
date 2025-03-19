# Write a menu-driven program to implement the Queue data structure. == FIFO

queue = ['11','12','13','14','15','16','17','18','19','20']

while True:
    print("\n\t1. Push element")
    print("\t2. Pop first element")
    print("\t3. Front element")
    print("\t4. Rear element")
    print("\t5. Display queue")
    print("\t6. Exit")

    choice = input(">>> Enter your choice: ")

    if choice == '1':
        item = input("Enter item to push: ")
        queue.append(item)
        print(f"{item} pushed to queue")
        print(queue)
    elif choice == '2':
        if len(queue):
            print("Popped first item:", queue[0])
            del queue[0]
            print(queue)
        else:
            print("queue is empty")
    elif choice == '3':
        if len(queue):
            print("Front item:", queue[0])
        else:
            print("queue is empty")
    elif choice == '4':
        if len(queue):
            print("Rear item:", queue[-1])
        else:
            print("queue is empty")
    elif choice == '5':
        print(queue)
    elif choice == '6':
        break
    else:
        print("Invalid choice, please try again.")
