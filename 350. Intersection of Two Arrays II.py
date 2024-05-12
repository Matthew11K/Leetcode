class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cntr = Counter(nums1)
        res = []
        for i in nums2:
            k = cntr.get(i)
            if k!= None and k>0:
                cntr[i]-=1
                res.append(i)
        return res
