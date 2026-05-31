class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1]*length

        for i in range(length):
            for index, j in enumerate(nums):

                if i == index:
                    continue
                result[i] = result[i]*j
        
        return result


        