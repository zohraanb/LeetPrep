from typing import List


# def twosum(nums, integer):
#     for i, n in enumerate(nums):
#         print(i)
#         if n > integer:
#             continue
#         for j, m in enumerate(nums, start= i):
#             if (n+m == integer):
#                 print(i, "," , j)
#                 return



# twosum([2, 7 , 11, 15], 9)

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