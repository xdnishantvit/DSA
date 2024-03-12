<<<<<<< HEAD
"""
Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.
"""


#User function template for Python

#User function template for Python

class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        for i in range(0,n):
            if k==arr[i]:
                return i
        else:
            return -1
        




#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


=======
"""
Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.
"""


#User function template for Python

#User function template for Python

class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        for i in range(0,n):
            if k==arr[i]:
                return i
        else:
            return -1
        




#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends