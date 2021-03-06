"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)                              # create a new node 
        self.length += 1
        if self.head and self.tail is None:                     # if there is no head
            self.head = new_node                                # if there is no node then we create one 
            self.tail = new_node                                # a single node is both the head and the tail 
        else:
            new_node.next = self.head                           # keep track of current head/ change in pointer 
            self.head.prev = new_node                           # change pointer 
            self.head = new_node                                # declare new head 


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value                                 #checking to make sure the value is at the tail 
        self.delete(self.head)
        return value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)                              # create a new node 
        self.length += 1                                        # keep track of the length 
        if self.head and self.tail is None:                     # if there is nothing in the list 
            self.head = new_node
            self.tail = new_node
        else:                                                   # add a new node to the end of the list 
            new_node.prev = self.tail                           # 
            self.tail.next = new_node
            self.tail = new_node


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value 
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)                                                      #delete node from current position
        self.add_to_head(node.value)                                           #add the node value to the head
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
        

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:                        # if LL is empty 
            print("Error there is nothing to delete") 
            return

        elif self.head == self.tail:                               # if its both 
            self.head = None                                       # delete the only node in the list 
            self.tail = None 

        elif node == self.head:                                    # if its the head        
            self.head = self.head.next                             # keep track of the new head
            node.delete()                                          # delete the node 
            
        elif node == self.tail:                                    # if its the tail
            self.tail = self.tail.prev
            node.delete()                                          # delete the node 

        else:                                                      # if its in the middle 
            node.delete()

        self.length -= 1                                           # keep track of length 
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        max_value = 0                                              # Max max var
        node.next +                                                # Loop through nodes via node.next
        if node.value > max_value:                                 # If node.value is higher, update max
        # return max
        pass
