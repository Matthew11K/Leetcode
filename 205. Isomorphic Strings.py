class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp = {}
        tSet = set()
        for i in range(len(s)):
            if s[i] not in mp:
                if t[i] in tSet:
                    return False
                mp[s[i]] = t[i]
                tSet.add(t[i])
            else:
                if mp[s[i]]!=t[i]:
                    return False
        return True