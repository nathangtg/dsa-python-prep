class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strA, strB = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            strA[s[i]] = strA.get(s[i], 0) + 1
            strB[t[i]] = strB.get(t[i], 0) + 1

        for i in strA:
            if strA[i] != strB.get(i, 0):
                return False

        return True