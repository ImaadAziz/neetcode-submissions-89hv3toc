import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapq.heapify_max(stones)
        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            temp = s1 - s2
            if temp != 0:
                heapq.heappush_max(stones, temp)
        
        if len(stones) == 1:
            return stones[0]
        return 0


        