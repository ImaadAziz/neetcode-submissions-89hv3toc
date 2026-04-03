class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashMap = {}
        for string in strs:
            temp = "".join(sorted(string))
            if temp in hashMap:
                hashMap[temp].append(string) 
            elif temp not in hashMap:
                tem = []
                tem.append(string)
                hashMap[temp] = tem
        res = list(hashMap.values())
        return res

        