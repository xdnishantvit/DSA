<<<<<<< HEAD
"""
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced"

"""


#User function Template for python3

class Solution:
    def ispar(self,x):
        stack = []
        for elem in x:
            if elem in ("{","(","["):
                stack.append(elem)
            else:
                if not stack:
                    return False
                
                elif self.isMatch(stack[-1],elem) == False:
                    return False
                
                else:
                    stack.pop()
                
        if stack:
            return False
        else:
            return True
            
    def isMatch(self,a,b):
        if (a == "(" and b ==")" ) or (a == "[" and b =="]" ) or (a == "{" and b =="}" ):
            return True
        else: 
            return False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
=======
"""
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced"

"""


#User function Template for python3

class Solution:
    def ispar(self,x):
        stack = []
        for elem in x:
            if elem in ("{","(","["):
                stack.append(elem)
            else:
                if not stack:
                    return False
                
                elif self.isMatch(stack[-1],elem) == False:
                    return False
                
                else:
                    stack.pop()
                
        if stack:
            return False
        else:
            return True
            
    def isMatch(self,a,b):
        if (a == "(" and b ==")" ) or (a == "[" and b =="]" ) or (a == "{" and b =="}" ):
            return True
        else: 
            return False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
