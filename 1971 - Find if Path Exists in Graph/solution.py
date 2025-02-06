class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei, visited):
                        return True
            return False
        visited = set()        
        return dfs(source, visited)
    

# Iterative solution using stack
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node):
            stack = [node]

            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
        visited = set()
        visited.add(source)
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        dfs(source)
        return destination in visited
'''    