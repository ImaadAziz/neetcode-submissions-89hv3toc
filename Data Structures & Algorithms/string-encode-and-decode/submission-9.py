class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        return res 

            
        
        return res

    def decode(self, s: str) -> List[str]:
        if s is None:
            return []
        res = []
        length = ""
        idx = 0
        while idx < len(s):
        
            temp = ""
            if s[idx] != "#":
                length += s[idx]
            if s[idx] == "#":
                print(length)
                length = int(length)
                for j in range(idx+1, idx+1+length):
                    temp += s[j]
                idx += length
                res.append(temp)
                length = ""
            
            idx += 1

                   
        

        return res
