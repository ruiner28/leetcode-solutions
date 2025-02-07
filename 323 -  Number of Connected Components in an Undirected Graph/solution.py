class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        def dfs(node):
            for j in graph[node]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
        ans = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                ans += 1
                visited.add(i)
                dfs(i)
        return ans        