class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Delete a node
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next


# Driver Code
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Linked List:")
ll.display()

ll.delete(20)

print("After Deletion:")
ll.display()