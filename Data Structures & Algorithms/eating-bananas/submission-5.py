import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num = max(piles)
        search_list = []
        lowest_rate = [max_num]


        # for i in range(1, max_num + 1):
        #     search_list.append(i)

        l, r = 1, max_num

        while l <= r:
            num = (l + r)//2


            time = 0
            for pile in piles:
                time += math.ceil(pile/num)
            
            if time <= h:
                r = num - 1
            
                if num < lowest_rate[0]:
                    lowest_rate[0] = num
            else:
                l = num + 1

        return lowest_rate[0]







        
