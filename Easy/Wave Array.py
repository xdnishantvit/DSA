"""
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

If there are multiple solutions, find the lexicographically smallest one.

Note:The given array is sorted in ascending order, and you don't need to return anything to make changes in the original array itself.
"""

from typing import List


class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        
        i, j = 0, 1 
        while j < len(arr):
            arr[i], arr[j] = arr[j], arr[i]
            
            i += 2
            j += 2
            
        return arr


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)
