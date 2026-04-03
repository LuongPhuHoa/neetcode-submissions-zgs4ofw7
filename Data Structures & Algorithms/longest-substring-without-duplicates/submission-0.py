class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        n = len(s)
        charSet = set()
        res = 0
        while r < n:
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                res = max(res, len(charSet))
            else:
                charSet.remove(s[l])
                l += 1
        return res