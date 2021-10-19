from typing import List

# Question 27: https://leetcode.com/problems/remove-element
# Removes given value from the list using list.pop() method
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        len1 = len(nums)
        if len(nums) == 0:
            return len(nums)
        while j <= len1:
            j += 1
            if len(nums) == 0 or i == len(nums):
                return len(nums)
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

nums = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(nums=nums, val=2))