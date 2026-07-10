class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        result = [1]*len(nums)

        for i,n in enumerate(nums):
            result[i] *= prefix
            prefix *= n
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
