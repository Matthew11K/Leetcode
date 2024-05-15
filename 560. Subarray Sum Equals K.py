class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        running_sum = 0
        ans = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            required_sum = running_sum - k

            if required_sum in sums:
                ans += sums[required_sum]
            if running_sum in sums:
                sums[running_sum] += 1
            else:
                sums[running_sum] = 1
        return ans