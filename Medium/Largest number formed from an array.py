<<<<<<< HEAD
"""
Given an array of strings arr[] of length n representing non-negative integers, arrange them in a manner, such that, after concatanating them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

"""


#User function Template for python3
class Solution:

    def printLargest(self, n, arr):
        # code here
        return ''.join(sorted(arr, key=functools.cmp_to_key(lambda a, b: -1 if a + b > b + a else 1)))
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

=======
"""
Given an array of strings arr[] of length n representing non-negative integers, arrange them in a manner, such that, after concatanating them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

"""


#User function Template for python3
class Solution:

    def printLargest(self, n, arr):
        # code here
        return ''.join(sorted(arr, key=functools.cmp_to_key(lambda a, b: -1 if a + b > b + a else 1)))
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends