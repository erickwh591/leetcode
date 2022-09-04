class Solution:
    def summaryRanges(nums: list[int]) -> list[str]:
        start_index = 0
        result = []

        for i in range(len(nums)):
            # Find last index for continuous series
            if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                continue

            if start_index == i:
                result.append(str(nums[start_index]))
            else:
                result.append(str(nums[start_index]) + "->" + str(nums[i]))

            start_index = i + 1

        return result

print(Solution.summaryRanges(nums = [0,2,3,4,6,8,9]))