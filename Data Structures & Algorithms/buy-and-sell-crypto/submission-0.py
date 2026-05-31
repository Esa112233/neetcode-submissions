class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        L = 0

        for i, R in enumerate(prices):
            print("L: ", L)
            print("R: ", R)
            profit = max(R  - prices[L], profit)

            if R - prices[L] < 0:
                L = i
        
        return profit


        