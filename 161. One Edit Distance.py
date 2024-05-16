class Solution:
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        m,n = len(s), len(t)
        count_diffr = 0
        if abs(m-n)>1:
            return False
        if m==n:
            for i in range(m):
                if s[i]!=t[i]:
                    count_diffr+=1
                if count_diffr > 1:
                    return False
            return count_diffr==1
        if m>n:
            s, t = t, s
            m,n=n,m
        i, j, diffr = 0, 0, 0
        while i < m and j < n:
            if s[i]!=t[j]:
                if diffr >= 1:
                    return False
                diffr += 1
                j += 1
            else:
                i+=1
                j+=1
        return True