class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # {"act": ["act", ""]}
        count = {}

        for st in strs:
            s = "".join(sorted(st))
            if s not in count:
                count[s] = []
    
            count[s].append(st)

        return list(count.values())