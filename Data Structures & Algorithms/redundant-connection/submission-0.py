class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet(len(edges)+1)
        for edge in edges:
            if not ds.unionBySize(edge):
                return edge

class DisjointSet:

    def __init__(self, n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]
        print(self.parent)
    
    def findUParent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.findUParent(self.parent[u])
        return self.parent[u]
    
    def unionBySize(self, edge):
        u,v = edge
        pu = self.findUParent(u)
        pv = self.findUParent(v)
        if pu == pv:
            return False
        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True
