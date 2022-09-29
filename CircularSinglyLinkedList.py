class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def insert(self, nodeValue, location):
        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.next = newNode
    
    def delete(self, location):
        if self.head is None:
            return "CircularSinglyLinkedList Empty."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode.next is not self.tail:
                        tempNode = tempNode.next
                    tempNode.next = self.tail.next
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextnode = tempNode.next
                tempNode.next = nextnode.next


    
cslinkedlist = CircularSinglyLinkedList()
cslinkedlist.insert(10,0)
cslinkedlist.insert(20,1)


cslinkedlist.insert(60,-1)



print([node.value for node in cslinkedlist])