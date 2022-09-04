class Solution:
    def canThreePartsEqualSum(arr: list[int]) -> bool:
        target = sum((arr))
        count = 0
        temp = 0
        for i in range(len(arr)):
            if temp + arr[i] != target / 3:
                temp += arr[i]
            else:
                temp = 0
                count += 1

        if count >= 3:
            return True
        return False
print(Solution.canThreePartsEqualSum(arr = [6,1,2,3,1,6]))