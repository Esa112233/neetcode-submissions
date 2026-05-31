class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # r_index - l_index = distance
        max_result = 0

        

        for l_index, i in enumerate(heights):
            r_index = len(heights) - 1


            while l_index < r_index:
                length = r_index - l_index
                r = heights[r_index]
                l = heights[l_index]
                h = 0

                if l < r:
                    h = l
                else:
                    h = r
                
                area = length*h
                if area > max_result:
                    max_result = area

                r_index -= 1
        
        return max_result
