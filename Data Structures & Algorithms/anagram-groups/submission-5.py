class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list) # automatically appends new key and list
        for word in strs:
            key = "".join(sorted(word)) # sort each word alphabetically and join
            groups[key].append(word) # for each key, append the matching word
        return list(groups.values())
        
        

        
            
        