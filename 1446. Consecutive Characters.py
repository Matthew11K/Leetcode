class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        m=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                m=max(m,count)
                count=1
        return max(count,m)