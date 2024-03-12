<<<<<<< HEAD
"""
Given a string s which contains only lower alphabetic characters, check if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string. Return true if it is possible to do else return false.

Note: The driver code print 1 if the value returned is true, otherwise 0.
"""


#User function Template for python3
class Solution:


    def getIdx(self,ch):
        return ord(ch) - ord('a')


    def allSame(self,freq, N):
        for i in range(0, N):
            if freq[i] > 0:
                same = freq[i]
                break

        for j in range(i + 1, N):
            if freq[j] > 0 and freq[j] != same:
                return False

        return True


    def sameFreq(self,str1):
        l = len(str1)


        freq = [0] * 26
        for i in range(0, l):
            freq[self.getIdx(str1[i])] += 1


        if self.allSame(freq, 26):
            return True

        for i in range(0, 26):

            if freq[i] > 0:
                freq[i] -= 1

                if self.allSame(freq, 26):
                    return True
                freq[i] += 1

        return False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T=int(input())

    for _ in range(T):
        s = input()
        ob = Solution()
        answer = ob.sameFreq(s)
        if answer:
            print(1)
        else:
            print(0)

=======
"""
Given a string s which contains only lower alphabetic characters, check if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string. Return true if it is possible to do else return false.

Note: The driver code print 1 if the value returned is true, otherwise 0.
"""


#User function Template for python3
class Solution:


    def getIdx(self,ch):
        return ord(ch) - ord('a')


    def allSame(self,freq, N):
        for i in range(0, N):
            if freq[i] > 0:
                same = freq[i]
                break

        for j in range(i + 1, N):
            if freq[j] > 0 and freq[j] != same:
                return False

        return True


    def sameFreq(self,str1):
        l = len(str1)


        freq = [0] * 26
        for i in range(0, l):
            freq[self.getIdx(str1[i])] += 1


        if self.allSame(freq, 26):
            return True

        for i in range(0, 26):

            if freq[i] > 0:
                freq[i] -= 1

                if self.allSame(freq, 26):
                    return True
                freq[i] += 1

        return False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T=int(input())

    for _ in range(T):
        s = input()
        ob = Solution()
        answer = ob.sameFreq(s)
        if answer:
            print(1)
        else:
            print(0)

>>>>>>> 16510f4966308b51e47e0ec74bd7f271f5d37b0a
# } Driver Code Ends