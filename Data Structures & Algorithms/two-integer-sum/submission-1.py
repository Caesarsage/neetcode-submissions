class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # i =0, num=3
        # diff = 7-3 =4
        # is diff 4 inside count, no
        # add: count = {3: 0}
        # i=1, num = 4
        # diff = 7-4 = 3
        # is the diff 3 in count, yes {3:0}
        # return [count[diff], i] = [count[3], 2] = [0, ]

        count = defaultdict()

        for i, v in enumerate(nums):
            diff = target - v
            if diff in count:
                return [count[diff], i]

            count[v] = i
        
        print(count)
        return []
        