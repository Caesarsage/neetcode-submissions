class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
    
        for s in strs:
            count = [0] * 26 #a --- z

            for c in s:
                index = ord(c) - ord("a") #using the ASCI value
                count[index] += 1
            res[tuple(count)].append(s) # conver to tuple so it mutable

        return res.values()


