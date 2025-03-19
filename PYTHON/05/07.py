# Write a menu-driven program to implement the stack data structure. == LIFO

stack = []

while True:
    print("\n\t1. Push element")
    print("\t2. Pop last element")
    print("\t3. Display stack")
    print("\t4. Exit")

    choice = input(">>> Enter your choice: ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.append(item)
        print(f"{item} pushed to stack")
        print(stack)
    elif choice == '2':
        if len(stack):
            print("Popped item:", stack.pop())
        else:
            print("Stack is empty")
    elif choice == '3':
        print(stack)
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
