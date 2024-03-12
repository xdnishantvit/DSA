"""
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
"""

#User function Template for python3


#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        lst1=sorted(array)
        leng=len(lst1)
        
        for i in range (0,leng) :
            if (lst1[i]!=i+1) :
                return i+1
                
        return (leng+1)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends