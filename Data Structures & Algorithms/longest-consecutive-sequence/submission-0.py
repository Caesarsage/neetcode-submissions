class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # <[100, 4, 200, 1, 3, 2]>

        # dry run
        # create a set from the initial array nums that will be use to check if there is a left and sequence
        # steps
        # which number does not have a left neighbor
        # 1st: 100
        # is there a left neighbor (i.e 99), no so start the sequence
        # 100 -> (is there 101). no. end sequence with lenght 1
        # 2nd iteration: 4
        # is theres a left neighbor (i.e 3), yes, so it's not a start of the sequence
        # 3rd iteration : 200
        # is there a left neighbor (i.e 199 ): no, so start the sequence
        # 200 -> (is there 201). no, end sequence (with length 1)
        # 4th iteration: 1
        # is there a left neighbor (i.e 0 ): no, so start the sequence
        # 1 -> (is there a 2), yes, continue
        # 1 -> 2 (is there a 3), yes, continue
        # 1 -> 2 -> 3 (is there a 4), yes continue
        # 1 -> 2 -> 3 -> 4 (is there a 5): no. end sequece with length 4) # is theres a left neighbor (i.e 3), yes, so it's not a start of the sequence
        # 5th iteration: 3
        # is theres a left neighbor (i.e 2), yes, so it's not a start of the sequence
        # 6th iteration: 2
        # is theres a left neighbor (i.e 1), yes, so it's not a start of the sequence

        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if it is the start of a sequence (left neighbor)
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length +=1

                longest = max(length, longest)

        return longest



