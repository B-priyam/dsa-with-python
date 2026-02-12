class Node:
    def __init__(self,item = None,next=None):
        self.item = item
        self.next = next

class Circular_linked_list:
    def __init__(self):
        self.last = None

    def insert_at_start(self,item):
        newNode = Node(item)
        if(self.last is None):
            newNode.next = newNode
            self.last = newNode
            return
        newNode.next = self.last.next
        self.last.next = newNode

    def insert_at_last(self,item):
        newNode = Node(item)
        if(self.last is None):
            newNode.next = newNode
            self.last = newNode
            return
        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

    def delete_start(self):
        if(self.last is None):
            return print("LL is sempty")
        if(self.last.next == self.last):
            self.last = None
            return
        self.last.next = self.last.next.next

    def delete_last(self):
        if(self.last is None):
            return print("LL is sempty")
        if(self.last.next == self.last):
            self.last = None
            return
        temp = self.last
        while temp.next is not self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp

    def print_ll(self):
        if(self.last == None): return
        temp = self.last.next
        while temp != self.last:
            print(temp.item,end=" ")
            temp = temp.next
        print(self.last.item,end=" ")
        
cll = Circular_linked_list()
cll.insert_at_start(10)
cll.insert_at_start(30)
cll.insert_at_start(40)
cll.insert_at_start(20)
cll.insert_at_last(5)
cll.insert_at_start(1)
cll.delete_start()
cll.delete_last()
cll.print_ll()