class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # {"act": ["act", "cat"]}
        res = defaultdict(list)

        for st in strs:
            count = [0]*26

            for c in st:
                count[ord(c) - ord('a')] +=1
            
            res[tuple(count)].append(st)

        return list(res.values())