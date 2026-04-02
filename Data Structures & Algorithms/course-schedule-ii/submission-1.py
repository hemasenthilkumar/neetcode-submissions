class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj =  defaultdict(set)
        dep = defaultdict(int)

        for courses,prereq in prerequisites:
            adj[prereq].add(courses)
            dep[courses] += 1

            adj[courses]
            dep[prereq]
        
        q = deque()
        for courses in range(numCourses):
            if dep[courses] == 0:
                q.append(courses)
        order = []
        while q:
            current = q.popleft()
            order.append(current)

            for courses in adj[current]:
                dep[courses] -= 1
                if dep[courses] == 0:
                    q.append(courses)
        if len(order) != len(dep):
            return []
        return order


