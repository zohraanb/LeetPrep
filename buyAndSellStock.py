from typing import List

# # my solution
# class Solution:

#     def maxProfit(self, prices:List[int]) -> int:
#         profit= 0
#         for i, n in enumerate(prices):
#             for j, m in enumerate(prices):
#                 if j<=i:
#                     continue
#                 if m - n > profit:
#                     print("m", m)
#                     print("n", n)
#                     profit = m-n

#         return profit

# solution = Solution()

# print(solution.maxProfit([7,1,5,3,6,4]))


class Solution:

    def maxProfit(self, prices:List[int]) -> int:
        profit= 0
        
        buy = prices[0]

        for price in prices[1:]:
            if price< buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy
        return profit
    
solution = Solution()

print(solution.maxProfit([7,1,5,3,6,4]))