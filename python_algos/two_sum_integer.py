from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in zip(range(len(nums)), range(len(nums))):
            print(f'i: {nums[i]}, j:{nums[j]}')


nums = [1,2,3,4,5]
solution = Solution()
solution.twoSum(nums, 4)

# output:
# i: 1, j:1
# i: 2, j:2
# i: 3, j:3
# i: 4, j:4
# i: 5, j:5

# * RANKED AS: EASY

# ? Given an array of integers nums and an integer target, ✅
# ? return the indices i and j such that nums[i] + nums[j] == target and i != j.
# ? You may assume that every input has exactly one pair of 
# ? indices i and j that satisfy the condition.
# ? Return the answer with the smaller index first.