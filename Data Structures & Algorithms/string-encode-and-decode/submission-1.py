class Solution:

    def encode(self, strs: List[str]) -> str:
        print("".join([str(len(s))+"$"+s for s in strs]))
        return "".join([str(len(s))+"$"+s for s in strs])

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            print("i=",i)
            j = i
            print("j=",j)
            while s[j] != "$":
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            print(s[j+1:j+1+length])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result