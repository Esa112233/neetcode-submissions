class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_nums = sorted(nums)

        sorted_len = len(nums)
        result = []

        for index, i in enumerate(sorted_nums):

            k = index + 1
            j = sorted_len -1
            while k < j and index < sorted_len - 2:

                s = i + sorted_nums[k] + sorted_nums[j]
                temp_arr = [i,  sorted_nums[k],  sorted_nums[j]]

                if s == 0:
                    if temp_arr not in result:
                        result.append(temp_arr)
                    j -=1
                    k +=1

                    while k < j and sorted_nums[k] == sorted_nums[k-1]:
                        k += 1
                    while j > k and j < sorted_len - 1 and sorted_nums[j] == sorted_nums[j+1]:
                        j -= 1
                if s > 0:
                    j -= 1
                if s < 0:
                    k += 1
            
        return result

        