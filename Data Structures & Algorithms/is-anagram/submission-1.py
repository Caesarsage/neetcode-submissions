class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict()
        count_t = defaultdict()

        for num in s:
            if num not in count_s:
                count_s[num] = 1
            else:
                count_s[num] +=1
        
        for num in t:
            if num not in count_t:
                count_t[num] = 1
            else:
                count_t[num] += 1
            
        return count_s == count_t