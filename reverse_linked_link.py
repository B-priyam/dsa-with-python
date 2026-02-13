class Node:
    def __init__(self,item = None, next=None):
        self.item = item
        self.next = next


class Singly_Linked_List:
    # start=None

    def __init__(self,item = None):
        self.start = item

    def insert_at_start(self,item):
        newNode = Node(item)
        newNode.next = self.start
        self.start = newNode

    def insert_at_last(self,item):
        newNode = Node(item)
        if(self.start is None):
            self.start = newNode
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def insert_after_data(self,data,item):
        temp = self.start
        while temp.next is not None and temp.item != data:
            temp = temp.next
        
        if(temp.item == data):
            newNode = Node(item)
            newNode.next = temp.next
            temp.next = newNode
        else:
            print("Cannot find data in LL")

    def delete_start(self):
        if(self.start is None):
            print("LL is empty")
            return
        self.start = self.start.next
    
    def delete_last(self):
        if(self.start is None):
            print("LL is empty")
            return 
        
        if(self.start.next is None):
            self.start = None
            return
        temp = self.start
        next = temp.next

        while next is not None and next.next is not None:
            next = next.next
            temp = temp.next        
        temp.next = None



    def print_sll(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next


    def rev_linked_list(self):
        prev = None
        curr = self.start
        while curr is not None:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward

        self.start = prev


sll = Singly_Linked_List()
sll.insert_at_start(40)
sll.insert_at_start(30)
sll.insert_at_start(20)
sll.insert_at_start(10)
sll.insert_at_start(5)
print()
# sll.rev_linked_list()
sll.print_sll()

