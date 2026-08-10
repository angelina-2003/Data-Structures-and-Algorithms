# params: 
#   - nums: array of integers
#   - Target: integer

# returns: Indexes of two numbers such that they add up to target


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index,num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need],index]
            seen[num] = index
        
        return []









# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         index = 0
#         index2 = 1 
#         while index < len(nums):
#             while index2 < len(nums):
#                 if nums[index] + nums[index2] != target:
#                     index2 += 1
#                 elif nums[index] + nums[index2] == target:
#                     return [index, index2]
#             index += 1
#             index2 = index + 1
            


    