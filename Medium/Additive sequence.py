"""
Given a string n, your task is to find whether it contains an additive sequence or not. A string n contains an additive sequence if its digits can make a sequence of numbers in which every number is addition of previous two numbers. You are required to complete the function which returns true if the string is a valid sequence else returns false. For better understanding check the examples.

Note: A valid string should contain at least three digit to make one additive sequence. 
"""




#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n):
        from sys import setrecursionlimit
        setrecursionlimit(2*10**3)
        ln=len(n)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i=0,j=1,k=2):
            nonlocal n,ln
            if k==ln:
                return 0
            sm=int(n[i:j])+int(n[j:k])
            lsm=len(str(sm))
            if int(n[k:k+lsm])==sm:
                if k+lsm==ln:
                    return 1
                elif dfs(j,k,k+lsm):
                    return 1
            if j+1<k and dfs(i,j+1,k):
                return 1
            return dfs(i,j,k+1)
        return dfs()


        #code here


#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends