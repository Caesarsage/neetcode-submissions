class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        count = {} #  value : index
        # {3: 0, 4: 1, 5: 2}


        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in count:
                return [count[diff], i]
            else:
                count[nums[i]] = i