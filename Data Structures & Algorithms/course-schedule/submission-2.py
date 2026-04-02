class Solution:
    from collections import defaultdict, deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        dep = defaultdict(int)
        # adj = pre-req: {courses}
        # dep = course: 0 (if no pre-req)
        for course, prereq in prerequisites:
            adj[prereq].add(course)
            dep[course] += 1

            adj[course]
            dep[prereq]
        
        q = deque()
        for course in range(numCourses):
            if dep[course] == 0:
                q.append(course)
    
        courses = 0
        while q:
            current = q.popleft()
            courses += 1

            for dependent_courses in adj[current]:
                dep[dependent_courses] -= 1
                if dep[dependent_courses] == 0:
                    q.append(dependent_courses)

        return courses==numCourses



