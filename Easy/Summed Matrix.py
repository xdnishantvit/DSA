<<<<<<< HEAD
"""
A matrix is constructed of size n*n. such that Mi,j= i+j. Count the number of cells having value q.
Note: Assume, the array is in 1-based indexing.
"""

#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        if q<2 or q>2*n:
            return 0
        elif q<=n+1:
            return q-1
        else:
            return 2*n-q+1
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,q=map(int,input().split())
        
        ob = Solution()
        print(ob.sumMatrix(n,q))
=======
"""
A matrix is constructed of size n*n. such that Mi,j= i+j. Count the number of cells having value q.
Note: Assume, the array is in 1-based indexing.
"""

#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        if q<2 or q>2*n:
            return 0
        elif q<=n+1:
            return q-1
        else:
            return 2*n-q+1
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,q=map(int,input().split())
        
        ob = Solution()
        print(ob.sumMatrix(n,q))
>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends