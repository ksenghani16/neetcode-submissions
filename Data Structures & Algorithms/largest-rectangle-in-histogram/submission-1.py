class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                height=heights[stack.pop()]
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                area=height*width
                max_area=max(max_area,area)
            stack.append(i)
        return max_area            


