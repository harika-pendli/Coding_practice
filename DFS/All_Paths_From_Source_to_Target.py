#Link:: https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        path=[]
        paths=[]
        dest= len(graph)-1
        def dfs(node):
            
            path.append(node)
            if node == dest:
                paths.append(path.copy())
                return
            
            neighbors= graph[node]
            
            for neighbor in neighbors:
                dfs(neighbor)
                path.pop()
            
        if len(graph)==0 or not graph:
            return paths
        dfs(0)
        
        return paths
        