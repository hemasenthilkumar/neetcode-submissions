class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sorted_cars = sorted(position, reverse=True)

        for car in sorted_cars:
            time = (target - car)/speed[position.index(car)]
            print(stack, time)
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)