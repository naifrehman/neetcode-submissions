class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # stores the freq of each element in nums
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        # seperate elements(keys) and their freq's to lists
        elementsInList = list(freq.keys())
        frequency = list(freq.values())

        # loop k times and get maxFrequency, get index, append element
        result = []
        for i in range(k):
            maxFrequency = max(frequency)
            index = frequency.index(maxFrequency)

            result.append(elementsInList[index])

            elementsInList.pop(index) # pop functions takes index of elem
            frequency.pop(index)

        return result
        
        
        
        
        