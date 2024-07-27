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
            new_node.next = None
            new_node.previous = None
            self.head = self.tail = new_node
        if temp and temp.data:
            new_node.next = self.head
            temp.previous = new_node
            new_node.previous = None
            self.head = new_node
    
    # Insert at end of the doubly linked list
    def insert_at_end(self, data):
        temp = self.tail;
        new_node = Node(data)
        if not temp:
            new_node.next = None
            new_node.previous = None
            self.head = self.tail = new_node
        if temp and temp.data:
            new_node.previous = self.tail
            temp.next = new_node
            new_node.next = None
            self.tail = new_node

    # Insert after a given node 
    def insert_after_node(self, node, data):
        temp = self.head
        found_node = None
        if node == self.tail.data:
            self.insert_at_end(data)
            return
        while temp:
            if temp.data == node:
                found_node = temp
                break
            temp = temp.next

        if found_node:
            new_node = Node(data)
            new_node.next = found_node.next
            new_node.previous = found_node
            if found_node.next:
                found_node.next.previous = new_node
            found_node.next = new_node

    # Insert before a given node
    def insert_before_node(self, node, data):
        temp = self.head
        found_node = None
        if node == temp.data:
            self.insert_at_beginnig(data)
            return
        while temp:
            if temp.data == node:
                found_node = temp
                break
            temp = temp.next
        if found_node:
            new_node = Node(data)
            new_node.next = found_node
            new_node.previous =  found_node.previous
            if found_node.previous:
                found_node.previous.next = new_node
            found_node.previous = new_node

    # Reverse traversal
    def reverse_traversal(self):
        temp = self.tail
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.previous
        print("<->".join(elements))

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
doubly_linked_list.insert_after_node(6,5)
doubly_linked_list.insert_after_node(5,1)
doubly_linked_list.insert_before_node(3, 4)
doubly_linked_list.insert_before_node(3,7)
doubly_linked_list.display_doubly_linked_list()
print('----------------------------')
doubly_linked_list.reverse_traversal()