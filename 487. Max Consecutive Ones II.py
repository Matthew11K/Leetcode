from typing import (
    List,
)

class Solution:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        left = 0
        maxLen = 0
        nel = len(nums)
        cntr = 0
        for right in range(nel):
            if nums[right] == 0:
                cntr +=1
            while cntr > 1:
                if nums[left] == 0:
                    cntr -=1
                left +=1
            maxLen = max(maxLen, right - left + 1)
        return maxLen
