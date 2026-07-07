class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for temp in range(len(temperatures)):
            current_temp = temperatures[temp]
            while stack and current_temp > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = temp - top
            stack.append(temp)
        return result
