class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueValues = set()
        l, r = 0, 0
        length = 0
        while r < len(s):
            while s[r] in uniqueValues:
                uniqueValues.remove(s[l])
                l+=1
            uniqueValues.add(s[l])
            uniqueValues.add(s[r])
            length = max(length, len(uniqueValues))
            r+=1
        return length