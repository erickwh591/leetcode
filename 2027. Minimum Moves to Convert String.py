class Solution:
    def minimumMoves(s: str) -> int:
        count = 0
        n = 0
        while n < len(s):
            if s[n] == 'X':
                n += 3
                count += 1
            else:
                n += 1

        return count

print(Solution.minimumMoves(s = "OXOXOX"))