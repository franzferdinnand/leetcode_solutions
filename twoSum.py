from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for num1 in range(n - 1):
            for num2 in range(num1 + 1, n):
                if nums[num1] + nums[num2] == target:
                    return [num1, num2]


x1 = Solution().twoSum([3, 2, 3], 6)
print(x1)