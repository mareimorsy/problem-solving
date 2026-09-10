class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(heights) -1
        while i < j:
            area = min(heights[i], heights[j]) * (j-i)
            max_water = max(max_water, area)

            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i +=1
                j -=1
            
        return max_water
        