
class Node:
    """
    Implements a node class for the queue data structure.
    """
    def __init__(self, value):
        # value of the node.
        self.value = value
        # pointer to the next node.
        self.next = None

class Queue:
    """
    
    Implements the queue datastructure.
    
    """

    def __init__(self):

        # initialize front and rear references.
        self.front = None
        self.rear = None
    
    def enqueue(self, item):
        """
        Performs the enqueue operation.

        params:
            - item : 
                item that needs to be enqueued.
        """
        
        # create current node.
        current_node = Node(item)

        # if rear exists.
        if self.rear is not None:
            #update pointer to new node.
            self.rear.next = current_node

        # update rear.
        self.rear = current_node
        
        # if queue is empty.
        if self.front is None:
            self.front = current_node


    def dequeue(self):
        """
        Performs the dequeue operation.

        returns:
            - value:
                value of the item that is dequeued.
        """

        # if queue is empty.
        if self.isEmpty():
            return

        # get value of node at the front.
        value = self.front.value

        # update front pointer.
        self.front = self.front.next

        # if only one item is left
        # set front and rear to None.
        if self.front is None:
            self.rear = None
        
        return value
    
    def peek(self):
        """
        Peeks at the front of the queue.

        returns:
            - front_value:
                value of the front node.
        """
        # return value at the front.
        return self.front.value
    
    def isEmpty(self):
        """
        Checks if queue is empty.

        returns:
            - isEmpty (bool):
                True if queue is empty else False.
        """

        # check if front is none.
        # if it is then the queue is empty.
        return self.front == None
