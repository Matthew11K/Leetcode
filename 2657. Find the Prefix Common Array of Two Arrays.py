class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        a = set()
        b = set()
        count = 0
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            if A[i]==B[i]:
                count += 1
                res.append(count)
                continue
            if A[i] in b:
                count += 1
            if B[i] in a:
                count += 1
            res.append(count)
        return res