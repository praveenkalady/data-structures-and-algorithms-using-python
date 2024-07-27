# Doubly linked list

# Creation of Node class

class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    # Insert at beginning
    def insert_at_beginnig(self, data):
        temp = self.head
        new_node = Node(data)
        if not temp:
            self.head = self.tail = new_node
        if temp and temp.data:
            new_node.next = self.head
            new_node.previous = None
            self.head = new_node
    
    def insert_at_end(self, data):
        temp = self.tail;
        print(temp.data,"temp")
        new_node = Node(data)
        if not temp:
            self.head = self.tail = new_node
        if temp and temp.data:
            new_node.previous = self.tail
            temp.next = new_node
            new_node.next = None
            self.tail = new_node

    # Display/Traversal through Doubly linked list

    def display_doubly_linked_list(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        if elements:
            print("<->".join(elements))
        else:
            print("No elements found!")



doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_at_beginnig(2)
doubly_linked_list.insert_at_beginnig(6)
doubly_linked_list.insert_at_beginnig(3)
doubly_linked_list.insert_at_end(9)
doubly_linked_list.display_doubly_linked_list()