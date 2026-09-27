class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[]for _ in range(numCourses)]
        for a,b in prerequisites:
            adj_list[a].append(b)
        visited=[0]*numCourses
        path_visited=[0]*numCourses
        for i in range(numCourses):
            if visited[i]==0:
                ans=self.dfs(i,visited,path_visited,adj_list)
                if ans==False:
                    return False
        return True

    def dfs(self,node,visited,path_visited,adj_list):
        visited[node]=1
        path_visited[node]=1
        for adjnode in adj_list[node]:
            if visited[adjnode]==0:
                x=self.dfs(adjnode,visited,path_visited,adj_list)
                if x==False:
                    return False
            elif path_visited[adjnode]==1:
                return False
        path_visited[node]=0
        return True 
                
        