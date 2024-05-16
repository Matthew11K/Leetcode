class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranges = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        if nums[-1] == start:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(nums[-1]))
        return ranges

