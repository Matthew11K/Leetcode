class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        subSet = set()
        maxLen = 0
        for right in range(n):
            if s[right] not in subSet:
                subSet.add(s[right])
                maxLen = max(maxLen, right - left + 1)
            else:
                while s[right] in subSet:
                    subSet.remove(s[left])
                    left+=1
                subSet.add(s[right])
        return maxLen
