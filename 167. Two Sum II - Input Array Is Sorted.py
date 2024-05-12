class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left+1,right+1]
            mid = (left+right)//2
            if cur_sum < target:
                if numbers[mid] + numbers[right] <= target:
                    left = mid
                else:
                    left += 1
            else:
                if numbers[mid] + numbers[left] >target:
                    right = mid
                else:
                    right -= 1