class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[last_non_zero] = nums[cur]
                last_non_zero += 1
        for zero in range(last_non_zero, len(nums)):
            nums[zero] = 0
