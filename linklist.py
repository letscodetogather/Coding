
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList():
    def __init__(self):
        self.head = None

    def insertAtBegining(self, value):
        newNode = Node(value)
        if self.head == None:
            newNode.next = None
        else:
            newNode.next = self.head

    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            return
        t_node = self.head
        while(t_node.next != None):
            t_node = t_node.next
        t_node.next = newNode


l = LinkList()
l.insertAtBegining(5)
