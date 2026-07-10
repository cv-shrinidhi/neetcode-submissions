class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLocation = {}
        total = 0
        for i,n in enumerate(nums):
            total = target - n
            if (total in numLocation):
                return [numLocation[total],i]
            else:
                numLocation[n] = i
        