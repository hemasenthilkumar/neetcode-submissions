class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)
        for i in range(len(heights)):
            new_start_index = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                width =(i - index)
                max_area = max(max_area, width*height)
                new_start_index = index
            stack.append([new_start_index, heights[i]])
        
        while stack:
            index, height = stack.pop()
            width = n - index
            max_area = max(max_area, width*height)

        return max_area
