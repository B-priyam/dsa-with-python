class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.item = item
        self.next = next
        self.prev = prev

class circular_doubly_linked_list:
    def __init__(self):
        self.start = None

    def insert_at_start(self,item):
        newNode = Node(item)
        if(self.start is None):
            newNode.next = newNode
            newNode.prev = newNode
            self.start = newNode
            return
        newNode.next = self.start
        newNode.prev = self.start.prev
        self.start.prev.next = newNode
        self.start.prev = newNode
        self.start = newNode

    def insert_at_last(self,item):
        newNode = Node(item)
        if(self.start is None):
            newNode.next = newNode
            newNode.prev = newNode
            self.start = newNode
            return
        newNode.next = self.start
        newNode.prev = self.start.prev
        self.start.prev.next = newNode
        self.start.prev = newNode

    def insert_after(self,data,item):
        if self.start is None:
            print("LL is empty")
            return
        temp = self.start.next
        while temp is not self.start and temp.item != data:
            temp = temp.next

        if(temp.item == data):
            newNode = Node(item)
            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode
        else:
            print("data not present in LL")

    def delete_first(self):
        if(self.start is None):
            print("LL is empty")
            return
        
        if(self.start.next == self.start):
            self.start = None
            return
        
        self.start.prev.next = self.start.next
        self.start.next.prev = self.start.prev
        self.start = self.start.next

    def delete_last(self):
        if(self.start is None):
            print("LL is empty")
            return
        
        if(self.start.next == self.start):
            self.start = None
            return
        
        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev

    def print_ll(self):
        if(self.start is None):
            print("LL is empty")
            return
        temp = self.start.next
        print(self.start.item,end=" ")
        while temp is not self.start:
            print(temp.item,end=" ")
            temp = temp.next
        

cdll = circular_doubly_linked_list()
cdll.insert_at_start(10)
cdll.insert_at_start(20)
cdll.insert_at_last(50)
cdll.insert_at_last(60)
cdll.insert_at_start(1)
cdll.insert_at_last(70)
cdll.insert_after(50,55)
cdll.delete_first()
cdll.delete_last()
cdll.insert_at_start(0)
cdll.insert_at_last(100)
cdll.print_ll()