class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        for e in edges:
            ds.unionBySize(e)
        parents = [ds.findUParent(i) for i in range(n)]
        return len(set(parents))

class DisjointSet:

    def __init__(self, n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]
    
    def findUParent(self, u):
        if u == self.parent[u]:
            print(u)
            return u
        self.parent[u] = self.findUParent(self.parent[u])
        return self.parent[u]
    
    def unionBySize(self, edge):
        u,v = edge
        pu = self.findUParent(u)
        pv = self.findUParent(v)
        if pu == pv:
            return
        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
