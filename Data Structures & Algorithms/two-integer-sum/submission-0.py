class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            target_value = target - nums[i]
            if target_value in dic:
                return [dic[target_value], i]
            dic[nums[i]] = i
        return []
        
    
# {
#     3 - 0
#     4 - 1
#     5 - 2
#     6 - 3
# }
# 7-3 = 4
