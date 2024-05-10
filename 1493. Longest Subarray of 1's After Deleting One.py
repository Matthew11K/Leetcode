class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur_len=0
        prev_len=0
        max_len=0
        for n in nums:
            if n==1:
                cur_len+=1
            else:
                prev_len=cur_len
                cur_len=0
            max_len=max(max_len,cur_len+prev_len)
        if max_len==len(nums):
            max_len-=1
        return max_len