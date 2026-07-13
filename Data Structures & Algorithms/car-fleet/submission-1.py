class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        stack = []
        # this uses intersection logic
        # if second last car time to reach target is less
        # than last car then they become a fleet and 
        # travel at last car's speed
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)