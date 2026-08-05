class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      
        max_area=0
        for i in range(len(heights)):
            min_height=heights[i]
            for j in range(i,len(heights)):
                if heights[j]<min_height:
                    min_height=heights[j]
                area=(min_height)*(j-i+1)
                max_area=max(max_area,area)
        return max_area

