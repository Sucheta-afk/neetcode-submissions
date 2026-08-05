class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build graph
        graph=defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap=[(0, k)]
        max_time=0
        visited=set()

        while heap:
            curr_time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            max_time=max(max_time, curr_time)

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (curr_time+weight, nei))
        if len(visited) != n:
            return -1
        return max_time
        