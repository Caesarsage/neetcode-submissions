class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for c in s:
            count_s[c] = 1 + count_s.get(c, 0)
       
        for d in t:
            count_t[d] = 1 + count_t.get(d, 0)
       
        print(count_s)
        print(count_t)
        return count_s == count_t