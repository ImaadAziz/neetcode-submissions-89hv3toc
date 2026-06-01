class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length)+ "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        length = ""
        idx = 0
        while idx < len(s):
            if s[idx] != "#":
                length += s[idx]
            if s[idx] == "#":
                length = int(length)
                temp = ""
                for i in range(idx+1,idx+length+1):
                    temp += s[i]
                res.append(temp)
                idx += length
                length = ""
            idx += 1
        

                
        return res
            