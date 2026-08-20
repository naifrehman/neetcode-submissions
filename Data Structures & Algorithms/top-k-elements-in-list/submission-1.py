class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # need a dict to store value and its freq
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        keys = list(freq.keys())
        values = list(freq.values())
        
        result = [] # final list to return

        for i in range(k):
            maxValue = max(values) # max freq from the list array
            index = values.index(maxValue) # values list, return index of maxValue  
            result.append(keys[index]) # append to list

            values.pop(index) # remove the value at the index
            keys.pop(index)

        return result 


        
        
        
        
        