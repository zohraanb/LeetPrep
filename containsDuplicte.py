from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}
        dups = False
        for i, num in enumerate(nums):
            if num in dupMap:
                dups = True
                return True
            else:
                dupMap[num] = i
        return False
    

solution = Solution()

print(solution.containsDuplicate([1,2,3,4]))
