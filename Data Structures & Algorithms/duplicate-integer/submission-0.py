class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash =  dict()
        for num in nums:
            if num in hash:
                hash[num] += 1
                if hash[num] > 1:
                    return True
            else:
                hash[num] = 1
            
        return False
        