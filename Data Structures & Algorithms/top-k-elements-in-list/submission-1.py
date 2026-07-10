class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach
        # n=total number of elements in the list, u=unique number of elements in the list
        freqDict = {n: nums.count(n) for n in set(nums)} #takes O(n*u)
        print(freqDict)
        sortedDict = dict(sorted(freqDict.items(), key=lambda x:x[1], reverse=True)) # takes O(ulogu)
        print(sortedDict)
        return list(sortedDict.keys())[:k]
        