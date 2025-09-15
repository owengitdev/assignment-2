# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    

# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):  # Most of the code I got it from Linked List Tutorial(Additional Resource)
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node

            return
        last = self.head
        while last.next:
            last= last.next
        last.next = new_node

    def remove(self):
        if self.head is None:
            return "The List is empty"
        self.head = self.head.next
        return None


def waitlist_generator():
    # Create a new linked list instance
    llist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
The list works like a system that has the data of names. You can add and remove any names if you don't want to include 
in the list.
- What role does the head play?
Head is one of the most important role in this Python since it can help detect any type-in from the user and system
can detect any anything that the user typed in. Head is important for analysis and letting the user to see the full 
output. 
- When might a real engineer need a custom list like this?
If a real engineer wanted a custom list like this one, I believe that the engineer might possibly further advanced list
than before like from normal LinkedList to the biggest list in python coding.
'''
