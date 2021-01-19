def buyAndSellStock(prices):
    p1 = 0
    p2 = 0
    profit = 0
    while(p2 < len(prices)):
        if prices[p2] < prices[p1]:
            p1 = p2
        else:
            diff = prices[p2] - prices[p1]
            if diff > profit:
                profit = diff
        p2 += 1
    return profit
        