from Node import Node

class LinkedList(object):
    def __init__(self):
        self.head=None
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while(current.next):
                current=current.next
            current.next=new_node
    def get(self,idx):
        pass
    def insert(self,idx,value):
        pass
    def delete(self,idx):
        pass