
class Node:
    """
    Implements a node class for the queue data structure.
    """
    def __init__(self, value):
        # value of the node.
        self.value = value
        # pointer to the next node.
        self.next = None

class SinglyLinkedList:
    """
    This implements the Singly Linked List Datastructure.
    """

    def __init__(self, head_val=None):
        # initialize head.
        self.head = Node(head_val) if head_val else None
    
    def insert(self, value):
        """
        Inserts a node into the linked list.
        
        params:
            - value :
                Value of the node to be inserted.
        returns:
            - nothing.
        """
        # node to be inserted.
        curr_node = Node(value)

        # if linked list is empty.
        if not self.head:
            self.head = curr_node
        else:
            # temp node for traversal.
            node = self.head

            while node.next is not None:
                node = node.next

            # add node at the tail.
            node.next = curr_node
        return 

    def traverse(self):
        """
        Traverses the linked list and prints it out.
        """
        # temp node for traversal.
        node = self.head

        # traverse the linked list and print it.
        while node:
            print(f"{node.value}", end=" -> ")
            node = node.next
        print()

    def delete(self, del_val):
        """
        Deletes a node if the value of node exists.

        params:
            - del_val:
                Value of the node that needs to be deleted.
        returns:
            - nothing.
        """

        # if del_val is head.
        if self.head:
            if self.head.value == del_val:
                self.head = self.head.next
                return
        
        # keep two pointers for deleting node.
        p1 = p2 = self.head

        while p2 is not None:
            # if delete value found.
            if p2.value == del_val:
                break
            # move pointers through ll.
            p1 = p2
            p2 = p2.next
        
        # if del_value not found.
        if p2 is None:
            print("Value not found!")
        
        # unlink node if del_val is matched.
        p1.next = p2.next
        p2 = None
        print("Node Deleted!")
        

        