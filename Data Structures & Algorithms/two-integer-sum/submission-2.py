class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = dict()

        for i, num in enumerate(nums):
            lookup[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup and i != lookup[diff]:
                return [i, lookup[diff]]

