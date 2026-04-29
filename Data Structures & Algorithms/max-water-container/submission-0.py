class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        
        while l<r:
            length = (r - l)
            breadth = min(heights[l], heights[r]) # min height
            area = length * breadth
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l +=1
        
        return maxArea

        