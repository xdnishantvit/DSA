<<<<<<< HEAD
"""
Given a string S, check if it is palindrome or not
"""

#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        x=S
        y=x[::-1]
        if x==y:
            return 1
        else:
            return 0
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPalindrome(S)
        print(answer)

=======
"""
Given a string S, check if it is palindrome or not
"""

#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        x=S
        y=x[::-1]
        if x==y:
            return 1
        else:
            return 0
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPalindrome(S)
        print(answer)

>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends