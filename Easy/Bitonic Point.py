"""
Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.
Note: If the array is increasing then just print the last element will be the maximum value

"""

#User function Template for python3
class Solution:

    def findMaximum(self,arr, n):
        # code here
        l = 0
        r = n - 1
        
        while(l < r):
            mid = (l + r) // 2
            if arr[mid] >= arr[mid + 1] and arr[mid] >= arr[mid  - 1]:
                return arr[mid]
            elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
            
        if arr[r] == arr[l]:
            return arr[l]
        return arr[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends