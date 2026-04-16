class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0

        # multiply difference between the bar and the distance

        for i in range(len(heights)):
            for j in range(len(heights)):
                dist = abs(i - j)
                currarea = dist * min(heights[i],heights[j])
                if currarea > max:
                    max = currarea

        return max