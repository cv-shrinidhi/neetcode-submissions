class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach
        freqDict = {n: nums.count(n) for n in set(nums)}
        print(freqDict)
        sortedDict = dict(sorted(freqDict.items(), key=lambda x:x[1], reverse=True))
        print(sortedDict)
        return list(sortedDict.keys())[:k]