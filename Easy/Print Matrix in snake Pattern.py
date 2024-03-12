"""
Given a matrix of size N x N. Print the elements of the matrix in the snake like pattern depicted below.
"""

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here
       sol=[]
       flag=True
       for row in matrix:
           if flag:
               sol.extend(row)
               flag=False
           else:
                sol.extend(row[::-1])
                flag=True
       return sol

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends