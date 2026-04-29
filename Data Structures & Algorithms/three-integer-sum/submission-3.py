class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]

            if a > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                # skip that i iteration
                continue
            
            # now do, two pointers for the remaining twoSum
            l = i+1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    r -=1

                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

        # for i, v in enumerate(sortedNums):
        #     if v > 0:
        #         break
            
        #     if i > 0 and v == sortedNums[i-1]:
        #         continue
            
        #     l = i+1
        #     r = len(sortedNums) - 1

        #     while l < r:
        #         threeSum = v + sortedNums[l] + sortedNums[r]
        #         if threeSum > 0:
        #             r -= 1
        #         elif threeSum < 0:
        #             l +=1
        #         else:
        #             res.append([v, sortedNums[l], sortedNums[r]])
        #             l +=1
        #             r -=1
                
        #             while sortedNums[l] == sortedNums[l-1] and l < r:
        #                 l+=1

        # return res


# [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1, 2]
# res;
# first iteration, v = -4, i = 0
# v = -4
# l = i+1 = 1
# r = len(nums) - 1 = 6
# while l < r:
# sum = -4 + nums[l] + nums[r] = -4 + (-1) + (2) = -3
# if sum > 0, reduce the right
        