class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        smap, tmap = {}, {}
        for x in range(len(s)):
            smap[s[x]] = 1+smap.get(s[x], 0)
            tmap[t[x]] = 1+tmap.get(t[x], 0)
        return smap == tmap