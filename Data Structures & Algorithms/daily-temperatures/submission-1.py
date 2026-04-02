class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                val = stack.pop()
                result[val[1]] = i-val[1]
            stack.append((temperatures[i], i))
        return result
