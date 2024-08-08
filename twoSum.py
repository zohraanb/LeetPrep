from typing import List

# my solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums):
#             if n > target:
#                 continue
#             for j, m in enumerate(nums):
#                 if j == i:
#                     continue
#                 elif (n+m == target):
#                     return(i,j)
#         return

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {}
        for i,n in enumerate(nums):
            diff = target - n 
            if (diff in hashMap):
                return hashMap[diff], i
            hashMap[n] = i 
        return

solution = Solution()

print(solution.twoSum([2,7,11,15], 9))