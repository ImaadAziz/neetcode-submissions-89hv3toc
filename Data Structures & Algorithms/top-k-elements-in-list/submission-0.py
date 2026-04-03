class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = []
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        
        for i in range(k):
            keyMax = max(res, key=res.get)
            res[keyMax] = 0
            counts.append(keyMax)
        
        return counts
