<<<<<<< HEAD
"""
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.

"""

#User function Template for python3

class Solution:
    def count(self, coins, N, amount):
        dp=[0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j]+=dp[j-coin]
        return dp[amount]
        # code here 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

=======
"""
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.

"""

#User function Template for python3

class Solution:
    def count(self, coins, N, amount):
        dp=[0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j]+=dp[j-coin]
        return dp[amount]
        # code here 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends