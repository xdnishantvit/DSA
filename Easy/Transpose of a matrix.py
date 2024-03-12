"""
Write a program to find the transpose of a square matrix of size N*N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.
"""

#User function Template for python3

class Solution:
    def transpose(self, matrix, n):
        # Write Your code here
        for i in range (n):
            for j in range (i + 1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
