class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        listS , listT = [], []
        for x in range(0, len(s)):
            listS.append(s[x])
            listT.append(t[x])

        if sorted(listS) == (sorted(listT)):
            return True
        else:
            return False