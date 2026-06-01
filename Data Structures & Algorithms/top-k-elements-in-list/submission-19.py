import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        
        
        heap = []
        for num, count in ct.items():
            heapq.heappush_max(heap, (count, num))

        sol = []
        for i in range(k):
            sol.append(heapq.heappop_max(heap)[1])
        
        return sol
