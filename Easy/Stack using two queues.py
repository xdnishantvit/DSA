<<<<<<< HEAD
"""
Implement a Stack using two queues q1 and q2.
"""

#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue   
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    if queue_1.full():
        return
    
    queue_2.put(x)
    
    while not queue_1.empty():
        queue_2.put(queue_1.get())
        
    
    queue_1, queue_2 = queue_2, queue_1
    
    # code here


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    if queue_1.empty():
        return -1
    
    return queue_1.get()
    # code here






#{ 
 # Driver Code Starts

from queue import Queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        queue_1 = Queue() # first queue
        queue_2 = Queue() # second queue
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1
            
        print()
=======
"""
Implement a Stack using two queues q1 and q2.
"""

#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue   
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    if queue_1.full():
        return
    
    queue_2.put(x)
    
    while not queue_1.empty():
        queue_2.put(queue_1.get())
        
    
    queue_1, queue_2 = queue_2, queue_1
    
    # code here


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    if queue_1.empty():
        return -1
    
    return queue_1.get()
    # code here






#{ 
 # Driver Code Starts

from queue import Queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        queue_1 = Queue() # first queue
        queue_2 = Queue() # second queue
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1
            
        print()
>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends