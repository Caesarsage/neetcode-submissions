class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # {"act": ["act", ""]}
        count = {}
        res = []

        for st in strs:
            s = "".join(sorted(st))
            if s not in count:
                count[s] = []
    
            count[s].append(st)

        print(count)       
    
        for v in count.values():
            res.append(v)

        return res
        