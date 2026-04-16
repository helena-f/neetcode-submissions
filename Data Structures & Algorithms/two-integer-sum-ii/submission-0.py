class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0 
        right = len(numbers) - 1

        currsum = 0
        while right > left:
            print(left, right)
            currsum = numbers[left] + numbers[right]
            print(currsum)
            if currsum == target:
                return [left+1,right+1]
            if currsum < target:
                left += 1
            if currsum > target:
                right -=1
        return []
            




