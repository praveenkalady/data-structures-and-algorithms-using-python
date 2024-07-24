# 1. Insertion at the Beginning: Adds a new node at the start of the list.
# 2. Insertion at the End: Adds a new node at the end of the list.
# 3. Deletion: Removes a node containing the specified data.
# 4. Search: Checks if a node with the specified data exists.
# 5. Traversal/Print: Prints the entire list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_node_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, data):
        del_node = self.head
        prev_node = None
        if del_node and del_node.data == data:
            self.head = del_node.next
            del_node.next = None
        if del_node and del_node.data != data:
            while del_node is not None:
                if del_node.data == data:
                    break
                prev_node = del_node
                del_node = del_node.next
            if del_node == None:
                return
            prev_node.next = del_node.next
            del_node = None
        print(prev_node.data)
        print(del_node)    

    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next  
        return False
    
    def display_data(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("->".join(elements))


singly_linked_list = SinglyLinkedList()
singly_linked_list.insert_node_at_beginning(1)
singly_linked_list.insert_node_at_end(3)
singly_linked_list.insert_node_at_end(7)
print(singly_linked_list.search_node(7))
singly_linked_list.delete_node(3)
singly_linked_list.display_data()