class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
    
        for st in strs:
            s_st = "".join(sorted(st))
            print(s_st)
            if s_st not in dic:
                dic[s_st] = [st]
            else:
                dic[s_st].append(st)

        print(dic)    
        return dic.values()

