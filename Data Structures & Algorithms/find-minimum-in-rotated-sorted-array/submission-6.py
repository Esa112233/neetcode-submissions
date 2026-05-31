class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[l] < nums[r]:
                return nums[l]

            middle = (l+r)//2
            res = min(nums[middle], res)
            
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle
        return res