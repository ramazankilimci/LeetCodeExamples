# Q35: Search Insert Position
# Given a sorted array of distinct integers and a target value
# return the index if the target is found. If not, return the index 
# where it would be if it were inserted in order...
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = int((start + end) / 2)
            if target == nums[mid]:
                return mid 
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start


nums = [1, 2, 3, 4, 5]
print(Solution().searchInsert(nums, 2))