class Node:
    def __init__(self,item= None, prev=None,next = None):
        self.item= item
        self.next = next
        self.prev = prev


class doubly_linked_list:
    def __init__(self,item = None):
        self.head = item
        self.tail = item

    def insert_at_head(self,item):
        newNode = Node(item)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            return

        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def insert_at_tail(self,item):
        newNode = Node(item)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def insert_after_data(self,data,item):
        if(self.tail.item == data):
            return self.insert_at_tail(item)
        if(self.head == None) :return
        temp = self.head
        while temp.next is not None and temp.item != data:
            temp = temp.next

        if(temp.item == data):
            newNode = Node(item)
            newNode.prev = temp
            newNode.next = temp.next
            temp.next = newNode
        else:
            print("Data not available in DLL")
        
    def delete_head(self):
        if(self.head == None):
            return print("LL is empty")
        if(self.head.next is None):
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None


    def delete_tail(self):
        if(self.tail == None):
            return print("LL is empty")
        if self.tail.prev is None:
            self.tail = None
            self.head  = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def print_dll(self):
        temp = self.head
        if temp is None :
            return
        print("head",self.head.item)
        print("tail",self.tail.item)
        while temp is not None:
            print(temp.item,end=" ")
            if(temp.next != None):
                print(" -> ",end="")
            temp = temp.next



dll = doubly_linked_list()
dll.insert_at_head(10)
dll.insert_at_tail(100)
dll.insert_at_head(20)
dll.insert_after_data(20,50)
dll.delete_head()
dll.delete_tail()
dll.print_dll()
    

        