<<<<<<< HEAD
"""
Given two sorted matrices mat1 and mat2 of size n x n of elements. Each matrix contains numbers arranged in strictly ascending order, with each row sorted from left to right, and the last element of a row being smaller than the first element of the next row. You're given a target value, x, your task is to find and count all pairs {a, b} such that a is from mat1 and b is from mat2 where sum of a and b is equal to x.
"""



#User function Template for python3
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        pairs = 0
        _set = set()
        
        for a in mat2:
            for b in a:
                _set.add(b)
        
        for i in range(n):
            for j in range(n):
                if x - mat1[i][j] in _set:
                    pairs += 1
        
        return pairs
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n , x = input().split()
        n,x = int(n), int(x)
        mat1 = []
        for _ in range(n):
            a = [int(x) for x in input().split()]
            mat1.append(a)

        mat2 = []
        for _ in range(n):
            a = [int(x) for x in input().split()]
            mat2.append(a)

        ob = Solution()
        ans = ob.countPairs(mat1, mat2, n, x)
        print(ans)

=======
"""
Given two sorted matrices mat1 and mat2 of size n x n of elements. Each matrix contains numbers arranged in strictly ascending order, with each row sorted from left to right, and the last element of a row being smaller than the first element of the next row. You're given a target value, x, your task is to find and count all pairs {a, b} such that a is from mat1 and b is from mat2 where sum of a and b is equal to x.
"""



#User function Template for python3
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        pairs = 0
        _set = set()
        
        for a in mat2:
            for b in a:
                _set.add(b)
        
        for i in range(n):
            for j in range(n):
                if x - mat1[i][j] in _set:
                    pairs += 1
        
        return pairs
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n , x = input().split()
        n,x = int(n), int(x)
        mat1 = []
        for _ in range(n):
            a = [int(x) for x in input().split()]
            mat1.append(a)

        mat2 = []
        for _ in range(n):
            a = [int(x) for x in input().split()]
            mat2.append(a)

        ob = Solution()
        ans = ob.countPairs(mat1, mat2, n, x)
        print(ans)

>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends