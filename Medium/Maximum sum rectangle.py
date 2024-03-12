<<<<<<< HEAD
"""
Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.
"""

#User function Template for python3
class Solution:
    def maximumSumRectangle(self,R,C,M):
        for r in M:
            for i in range(1, C):
                r[i] += r[i-1]
               
        ans = float('-inf') 
        for l in range(C):
            for r in range(l, C):
                running = 0
                for i in range(R):
                    v = M[i][r]
                    if l > 0:
                        v -= M[i][l-1]
                    running += v
                    ans = max(ans, running)
                    if running < 0:
                        running = 0
        return ans
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
=======
"""
Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.
"""

#User function Template for python3
class Solution:
    def maximumSumRectangle(self,R,C,M):
        for r in M:
            for i in range(1, C):
                r[i] += r[i-1]
               
        ans = float('-inf') 
        for l in range(C):
            for r in range(l, C):
                running = 0
                for i in range(R):
                    v = M[i][r]
                    if l > 0:
                        v -= M[i][l-1]
                    running += v
                    ans = max(ans, running)
                    if running < 0:
                        running = 0
        return ans
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends