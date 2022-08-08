class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adjacency_list={k:[] for  k in range(n)}
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
        
        #can remove this function and integrate with validPath to reduce runtime
        
        def dfs(adjacency_list,source,destination):
            marked= [False]*n
            flag=False
            stack=[source]
            while len(stack)>0:
                v=stack.pop()
                if v==destination:
                    flag=True
                
                if not marked[v]:
                    marked[v]=True
                    for w in adjacency_list[v]:
                        if not marked[w]:
                            stack.append(w)
            return flag
        
        
        return dfs(adjacency_list,source,destination)
                            
                
            
            
            
                
        
