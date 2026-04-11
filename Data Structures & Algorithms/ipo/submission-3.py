class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        maxHeap = []
        i = 0
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])  # max-heap via negative
                i += 1
    
            if not maxHeap:
                break  # no affordable projects
        
            # Take the most profitable
            w += -heapq.heappop(maxHeap)
            k -= 1

        return w