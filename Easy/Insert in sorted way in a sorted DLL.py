<<<<<<< HEAD
"""
Given a sorted doubly linked list and an element X, your need to insert the element X into correct position in the sorted DLL.

Note: The DLL is sorted in ascending order
"""

#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

def sortedInsert(head, x):
    temp = Node(x)
    curr = head
    
    if head == None:
        return temp
    
    if temp.data <= head.data:
        temp.next = head
        head.prev = temp
        return temp
    
    else:
        while curr.next != None and curr.next.data < temp.data:
            curr = curr.next
        temp.next = curr.next
        
        if curr.next != None:
            curr.next.prev = temp
            
        curr.next = temp
        temp.prev = curr
        return head
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node


def displayList(head):
    pvs=None
    while head:
        print(head.data, end=' ')
        if head.prev !=pvs:
            print('prev pointer not connected')
        pvs = head
        head = head.next
        


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        dll.head=sortedInsert(dll.head, x)
        displayList(dll.head)
        print()




=======
"""
Given a sorted doubly linked list and an element X, your need to insert the element X into correct position in the sorted DLL.

Note: The DLL is sorted in ascending order
"""

#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

def sortedInsert(head, x):
    temp = Node(x)
    curr = head
    
    if head == None:
        return temp
    
    if temp.data <= head.data:
        temp.next = head
        head.prev = temp
        return temp
    
    else:
        while curr.next != None and curr.next.data < temp.data:
            curr = curr.next
        temp.next = curr.next
        
        if curr.next != None:
            curr.next.prev = temp
            
        curr.next = temp
        temp.prev = curr
        return head
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node


def displayList(head):
    pvs=None
    while head:
        print(head.data, end=' ')
        if head.prev !=pvs:
            print('prev pointer not connected')
        pvs = head
        head = head.next
        


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        dll.head=sortedInsert(dll.head, x)
        displayList(dll.head)
        print()




>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends