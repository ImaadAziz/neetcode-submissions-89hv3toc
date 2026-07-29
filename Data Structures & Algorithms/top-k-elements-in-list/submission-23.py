class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        max_heap = []

        for i, count in ct.items():
            heapq.heappush(max_heap, (count * -1, i))

        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res