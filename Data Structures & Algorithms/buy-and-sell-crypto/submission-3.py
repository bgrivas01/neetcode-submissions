class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left+1
        profit = 0

        while right< len(prices):
            if prices[left]> prices[right]:
                left=right
                right+=1
            elif prices[right]> prices[left]:
                profitnew = prices[right]-prices[left]
                if profitnew >profit:
                    profit = profitnew
                    right+=1
                else:
                    right+=1
            else:
                right+=1

        return profit