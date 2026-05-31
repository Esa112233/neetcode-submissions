class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
        
        longest = 0
        temp = 0
        sequence_start = []

        for i in nums:
            if i-1 not in hashmap:
                sequence_start.append(i)
        length = len(sequence_start)

        for i in range(length):
            x = 1
            temp = 0
            while True:
                if sequence_start[i]+x in hashmap:
                    temp += 1
                    if temp > longest:
                        longest = temp
                else:
                    break
                x+=1
        return longest+1
                

