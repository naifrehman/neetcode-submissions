class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list) # used for creating a key: [] list 
        for word in strs: # iterate thru str array
            key = "".join(sorted(word)) # sort each str alphabetically and join
            groups[key].append(word) # 
        return list(groups.values())
        

        
            
        