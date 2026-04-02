"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        if not node.neighbors:
            return Node()
        copy = {}
        
        queue = collections.deque()
        visit = set()
        queue.append(node)
        while queue:
            n = queue.popleft()
            newnode = Node(n.val)
            visit.add(n.val)
            copy[n] = newnode
            for nei in n.neighbors:
                if nei.val not in visit:
                    queue.append(nei)
        for oldnode,newnode in copy.items():
            for nei in oldnode.neighbors:
                newnode.neighbors.append(copy[nei])
        
        return copy[node]