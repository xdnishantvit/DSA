<<<<<<< HEAD
"""
Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.
"""


#User function Template for python3

class Solution:
    def print2largest(self,arr, n):
        # code here
        arr.sort(reverse=True)
        for i in range(n):
            if (arr[i]!= arr[0]):
                return arr[i]
        return -1        



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

=======
"""
Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.
"""


#User function Template for python3

class Solution:
    def print2largest(self,arr, n):
        # code here
        arr.sort(reverse=True)
        for i in range(n):
            if (arr[i]!= arr[0]):
                return arr[i]
        return -1        



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends