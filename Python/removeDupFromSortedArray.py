# This script removes duplicates in a sorted array.
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        singular_elem = 0
        for i in range(len(nums)):
            if nums[i] != nums[singular_elem]:
                singular_elem += 1
                nums[singular_elem] = nums[i]
        
        return singular_elem + 1


list2 = [0,0,1,1,1,2,2,3,3,4]
obj1 = Solution()
print(obj1.removeDuplicates(nums=list2))
