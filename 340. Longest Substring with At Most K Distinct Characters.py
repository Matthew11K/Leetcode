from collections import defaultdict
class Solution:
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        nel = len(s)
        maxLen = 0
        left = 0
        cntr = defaultdict(int)
        for right in range(nel):
            cntr[s[right]] += 1
            while len(cntr) > k:
                cntr[s[left]] -= 1
                if cntr[s[left]] == 0:
                    del cntr[s[left]]
                left+=1
            maxLen = max(maxLen, right - left + 1)
        return maxLen