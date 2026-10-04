class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph=defaultdict(list)
        if len(edges)!=n-1:
            return False
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=[0]*n
        def dfs(node):
            visited[node]=1
            for nei in graph[node]:
                if visited[nei]==0:
                    dfs(nei)
        dfs(0)
        return sum(visited)==n