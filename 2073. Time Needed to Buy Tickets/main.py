class Solution:
    def timeRequiredToBuy(tickets: list[int], k: int) -> int:
        count = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i] > 0 and tickets[k] != 0:
                    tickets[i] -= 1
                    count += 1
        return count

print(Solution.timeRequiredToBuy(tickets = [5,1,1,1], k = 2))