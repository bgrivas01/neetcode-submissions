class Solution:
    def maxArea(self, heights: List[int]) -> int:
        newmax = 0
        left = 0
        right = len(heights)-1
        while left<right:
            if heights[left]<heights[right]:
                possible = heights[left] * (right-left)
                if possible > newmax:
                    newmax = possible 
                left+=1
            elif heights[right]<heights[left]:
                possible = heights[right]* (right-left)
                if possible > newmax:
                    newmax = possible 
                right-=1
            elif heights[right] == heights[left]:
                possible = heights[right]* (right-left)
                if possible > newmax:
                    newmax = possible
            
                left+=1
            
            
            

        return newmax
            