import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = []
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        
        heap = []
        for num, count in res.items():
            heapq.heappush_max(heap, (count, num))

        sol = []
        for i in range(k):
            sol.append(heapq.heappop_max(heap)[1])
        
        return sol
