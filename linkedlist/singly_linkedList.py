
class Node:
    '''
     __init__ method that initializes the linked list with an empty head, if head is initailize for first time
                 _______________
                |       |       |
    head -----> | data  |  next | -------> None
                |_______|_______| 
     
    '''
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self) -> object:
        self.head = None
        
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        else:
            new_node.next = self.head
            self.head = new_node
            
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            
            current.next = new_node
    
    def printLinkedList(self):
        current = self.head
        str_data = ''
        while current:
            str_data += f'{current.data} --> '
            current = current.next
        return str_data[:-4]
            
if __name__ == "__main__":
    
    linkedlist = Linkedlist()
    linkedlist.insertAtBegin('7')
    linkedlist.insertAtBegin(0)
    linkedlist.insertAtBegin(90)
    linkedlist.insertAtEnd(9)
    linkedlist.insertAtEnd('12')
    print(linkedlist.printLinkedList())
            
        
        
