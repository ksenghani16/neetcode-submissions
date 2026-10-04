class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        count=0
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=[0]*n
        def dfs(node):
            visited[node]=1
            for nei in graph[node]:
                if visited[nei]==0:
                    dfs(nei)
        for node in range(n):
            if visited[node]==0:
                count+=1
                dfs(node)
        return count
        