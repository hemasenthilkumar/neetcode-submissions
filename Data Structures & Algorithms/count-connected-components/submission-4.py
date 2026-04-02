from collections import defaultdict
class Solution:
    def traversal(self, adj, v, curr_node, output, visited):
        output.append(curr_node)
        nodes = adj.get(curr_node, [])
        for node in nodes:
            if visited[node] is False:
                visited[node] = True
                self.traversal(adj, v, node, output, visited)

    def countComponents(self, v: int, edges: List[List[int]]) -> int:
        # create adj map
        adj = defaultdict(list)
        for u,y in edges:
            adj[u].append(y)
            adj[y].append(u)
        output = []
        visited =[False]*(v+1)
        count = 0
        for i in range(v):
            if visited[i] is False:
                count += 1
                visited[i] = True
                self.traversal(adj, v, i, output, visited)
        return count
        