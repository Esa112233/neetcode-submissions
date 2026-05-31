class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while right >= left:
          middle = (right + left)//2
          guess = nums[middle]


          if guess == target:
            return middle
            
          elif guess > target:
                right = middle - 1
          elif guess < target:
                left = middle + 1
        return -1

        