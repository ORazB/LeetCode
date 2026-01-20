from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      buyPrice = prices[0]
      maxProfit = 0
      
      for i in range(1, len(prices)):
        if buyPrice > prices[i]:
          buyPrice = prices[i]
        
        maxProfit = max(maxProfit, prices[i] - buyPrice)
      return maxProfit