class Solution:
    def isPalindrome(self, s: str) -> bool:
        # my initial approach O(n)
        # chars = (''.join(a for a in s if a.isalnum())).lower()
        # return (chars == chars[::-1])
        # there can be ways this can be limited like 
        # dont use isalnum function and implement it yourself
        # or dont use extra space

        # better approach: 2-pointer
        l = 0
        r = len(s)-1

        while l<r:
            while l < r and not self.alphaNum(s[l]):
                l+=1
            while l < r and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))
            
