
class Node:
    """
    Implements a node class for the queue data structure.
    """
    def __init__(self, value):
        # value of the node.
        self.value = value
        # pointer to the next node.
        self.next = None
        # pointer to prev node.
        self.prev = None

class DoublyLinkedList:

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
            # update prev pointer.
            curr_node.prev = node
        return 
    
    def traverse(self):
        """
        Traverses the linked list and prints it out.
        """
        if self.head:
            # temp node for traversal.
            node = self.head
        else:
            print("Doubly Linked List is empty!")
            return

        # traverse the linked list and print it.
        while node:
            print(f"{node.value}", end=" <-> ")
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
                # break connection from new head to current head.
                if self.head.next:
                    self.head.next.prev = None
                # set new head.
                self.head = self.head.next
                print("Node Deleted!")
                return
        
        # keep pointer for deleting node.
        p =  self.head

        while p is not None:
            # if delete value found.
            if p.value == del_val:
                break
            # move pointers through ll.
            p = p.next
        
        # if del_value not found.
        if p is None:
            print("Value not found!")
        
        # unlink    al is matched.
        # set prev.next to next
        p.prev.next = p.next
        # set next.prev to prev
        if p.next:
            p.next.prev = p.prev
        print("Node Deleted!")