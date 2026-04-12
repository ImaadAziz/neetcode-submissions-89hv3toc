class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for s, d, t in times:
            adj[s].append([d, t])

        minHeap = [[0, k]]
        shortest = 0
        visited = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            shortest = t1
            visited.add(n1)

            for n2, t2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [t1 + t2, n2])
            
       
        if len(visited) != n:
            return -1
        return shortest