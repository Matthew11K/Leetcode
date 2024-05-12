class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLen = 0
        cnt_zero = 0
        nel = len(nums)
        for right in range(nel):
            if nums[right] == 0:
                cnt_zero += 1
            while cnt_zero > k:
                if nums[left] == 0:
                    cnt_zero -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen