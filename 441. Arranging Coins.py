class Solution:
    def arrangeCoins(n: int) -> int:
        res = 0
        start = 1
        while n > 0:
            n -= start
            start += 1
            res += 1
        if n == 0:
            res += 1
        return res - 1

print(Solution.arrangeCoins(n = 1))
