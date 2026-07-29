class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        heap = []
        for n, count in ct.items():
            heapq.heappush(heap, [count * -1, n])
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res