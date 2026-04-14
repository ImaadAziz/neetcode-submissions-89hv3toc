class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        minH = []
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            s, d = edges[i]
            adj[s].append([d, succProb[i]])
            adj[d].append([s, succProb[i]])

        probs = [(-1, start_node)]
        
        visit = set()
        while probs:
            prob, edge = heapq.heappop(probs)
            visit.add(edge)

            if edge == end_node:
                return prob * -1

            for e, p in adj[edge]:
                if e not in visit:
                    heapq.heappush(probs, (p * prob, e))

        return 0

        