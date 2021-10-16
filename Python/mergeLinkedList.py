class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


llist1 = LinkedList([1, 2, 4])
llist2 = LinkedList([1, 3, 4])
print(llist1)
print(llist2)

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    
    singleNode = LinkedList([0])
    tempNode = singleNode

    
    node1 = l1.head
    node2 = l2.head

    while True:
        if node1 is None:
            tempNode.next = node2
            break
        if node2 is None:
            tempNode.next = node1
            break
        
        if node1.data <= node2.data:
            tempNode.next = node1
            node1 = node1.next
        else:
            tempNode.next = node2
            node2 = node2.next
        
        tempNode = tempNode.next
    

    return singleNode.next
        
llist1.head = mergeTwoLists(llist1, llist2)
for i in llist1:
    print(i.data)

