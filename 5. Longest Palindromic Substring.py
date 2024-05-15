class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        res = ""
        for i in range(len(s)):
            var1 = isPalindrome(s,i,i)
            var2 = isPalindrome(s,i,i+1)
            if len(var1) > len(res):
                res = var1
            if len(var2) > len(res):
                res = var2
        return res
