class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force hashmap solution (not optimizes for space, the question need O(1)
        # [2,3,4], target = 6
        # 1st iteration, i = 0
        # tmp = 6 - 2 = 4, is "4" in count dict ? no, proceed
        # add to the count {number: index+1}, i.e count[numbers[i]] = i + 1
        # {2: 1}
        # 2nd iteration, i = 1
        # tmp = 6 - 3 = 3, is "3" in the count, no, proceed
        # {2:1, 3: 2}
        # 3rd iteration, i = 2
        # tmp = 6 - 4 = 2, is "2" in the count, yes, 2:1
        # return it's value and i+1, [1, i+1], [1,3]

        # count = defaultdict()

        # for i in range(len(numbers)):
        #     tmp = target - numbers[i]
        #     print(count)
        #     if tmp in count:
        #         return [count[tmp], i+1]
        #     count[numbers[i]] = i + 1
        
        # return [] 

# Two pointers solution gives O(1) space
        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -=1
            if curSum < target:
                l +=1
            if curSum == target:
                return [l+1, r+1]
        return []
        