class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashdic = {}

        print(hashdic)
        for i in range(len(nums)):
            if nums[i] not in hashdic:
                hashdic[nums[i]] = 1
            else:
                return True
        return False 

         