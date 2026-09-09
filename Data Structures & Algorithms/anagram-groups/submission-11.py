class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word)) # sort word and recombine to str
            groups[key].append(word) # for every word that matches key

        return list(groups.values())
        
        

        
            
        