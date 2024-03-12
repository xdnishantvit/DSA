<<<<<<< HEAD
"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
"""

#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        map = {}
        count = 0
        for i in range(n):
            if k - arr[i] in map:
                count += map[k - arr[i]]
            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
        return count
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

=======
"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
"""

#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        map = {}
        count = 0
        for i in range(n):
            if k - arr[i] in map:
                count += map[k - arr[i]]
            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
        return count
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends