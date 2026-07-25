class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            print("m=",m)
            if target == nums[m]:
                return m
            elif nums[m] >= nums[l]:
                print("in >= loop")
                if target >= nums[l] and target < nums[m]:
                    print("r shifted")
                    r = m-1
                elif target < nums[l] or target > nums[m]:
                    print("l shifted")
                    l = m+1
            else:
                print("in < loop")
                if target > nums[m] and target <= nums[r]:
                    print("l shifted")
                    l = m+1
                elif target > nums[r] or target < nums[m]:
                    print("r shifted")
                    r = m-1
        return -1