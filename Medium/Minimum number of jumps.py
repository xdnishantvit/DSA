<<<<<<< HEAD
"""
Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.

"""


#User function Template for python3

class Solution:
    def minJumps(self, arr, n):
    #code here
        n = len(arr)
 
        if n == 0 or arr[0] == 0:
            return -1
        if n==1 and arr[0]>1: return 0 
        jumps = 1  
        max_reach = arr[0]  
        steps_available = arr[0]  
        
        for i in range(1, n):
            if i == n - 1:
                return jumps
    
            max_reach = max(max_reach, i + arr[i])
            steps_available -= 1
    
            if steps_available == 0:
                jumps += 1
    
                if i >= max_reach:
                    return -1  
    
                steps_available = max_reach - i
    
        return -1 


 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
=======
"""
Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.

"""


#User function Template for python3

class Solution:
    def minJumps(self, arr, n):
    #code here
        n = len(arr)
 
        if n == 0 or arr[0] == 0:
            return -1
        if n==1 and arr[0]>1: return 0 
        jumps = 1  
        max_reach = arr[0]  
        steps_available = arr[0]  
        
        for i in range(1, n):
            if i == n - 1:
                return jumps
    
            max_reach = max(max_reach, i + arr[i])
            steps_available -= 1
    
            if steps_available == 0:
                jumps += 1
    
                if i >= max_reach:
                    return -1  
    
                steps_available = max_reach - i
    
        return -1 


 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends