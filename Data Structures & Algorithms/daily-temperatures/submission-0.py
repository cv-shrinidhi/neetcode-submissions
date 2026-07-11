class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # one element is a pair [temp,index]
        output = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp,stackIndex = stack.pop()
                output[stackIndex] = i-stackIndex
            stack.append([temp,i])
        return output
                