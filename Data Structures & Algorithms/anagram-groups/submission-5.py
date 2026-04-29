class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # charCout to list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)
        
        return list(res.values())




        # hashmap

        # for st in strs:
        #     sorted_st = ",".join(sorted(st))

        #     print(sorted_st) 
        #     if sorted_st not in count:
        #         count[sorted_st] = [st]
        #     else:
        #         count[sorted_st].append(st)

        # print(count)
        # return count.values()
  