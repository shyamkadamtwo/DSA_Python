class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, nodeValue, location):
        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
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
    
    def traverse(self):
        if self.head is None:
            return 'Linked List Empty'
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, searchValue):
        if self.head is None:
            return "Linked list is Empty"
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == searchValue:
                    return (index, node.value)
                node = node.next
                index += 1
            return "This value not found"

    def delete(self, location):
        if self.head is None:
            return "LinkedList Empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next.next is not None:
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                node.next = node.next.next







singlylinkedlist = SinglyLinkedList()
singlylinkedlist.insert(10,0)
singlylinkedlist.insert(20,0)
singlylinkedlist.insert(30,0)
singlylinkedlist.insert(40,0)
singlylinkedlist.insert(50,0)
singlylinkedlist.traverse()
print(singlylinkedlist.search(100))

print([node.value for node in singlylinkedlist])
singlylinkedlist.delete(-1)
singlylinkedlist.delete(-1)

print([node.value for node in singlylinkedlist])