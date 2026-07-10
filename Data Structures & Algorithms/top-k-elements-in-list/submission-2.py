class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach
        # n=total number of elements in the list, u=unique number of elements in the list
        # freqDict = {n: nums.count(n) for n in set(nums)} #takes O(n*u)
        # print(freqDict)
        # sortedDict = dict(sorted(freqDict.items(), key=lambda x:x[1], reverse=True)) # takes O(ulogu)
        # print(sortedDict)
        # return list(sortedDict.keys())[:k]

        # bucket sort variation
        countDict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countDict[num] = countDict.get(num,0) + 1
        print(countDict)
        for num, count in countDict.items():
            freq[count].append(num)
        print(freq)

        result = []
        for i in range(len(freq)-1, 0, -1):
            print(freq[i])
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
