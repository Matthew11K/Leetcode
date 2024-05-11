class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        i = 0
        left = height[i]
        j = len(height) - 1
        right = height[j]
        while i < j:
            if left <= right:
                sum += left - height[i]
                i += 1
                left = max(left, height[i])
            else:
                sum += right - height[j]
                j -= 1
                right = max(right, height[j])
        return sum