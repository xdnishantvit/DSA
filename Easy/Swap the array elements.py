<<<<<<< HEAD
"""
Given an array arr of n positive integers. The task is to swap every ith element of the array with (i+2)th element.
"""


#User function Template for python3

class Solution:
    def swapElements(self, arr, n):
        for i in range(n-2):
            arr[i], arr[i+2] = arr[i+2], arr[i]
    
        
        #Code here


#{ 
 # Driver Code Starts

#Initial Template for Python 3
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.swapElements(arr, n);
        for i in arr:
            print(i, end = " ")
        print()
=======
"""
Given an array arr of n positive integers. The task is to swap every ith element of the array with (i+2)th element.
"""


#User function Template for python3

class Solution:
    def swapElements(self, arr, n):
        for i in range(n-2):
            arr[i], arr[i+2] = arr[i+2], arr[i]
    
        
        #Code here


#{ 
 # Driver Code Starts

#Initial Template for Python 3
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.swapElements(arr, n);
        for i in arr:
            print(i, end = " ")
        print()
>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends