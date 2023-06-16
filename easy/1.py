class Solution:
    def twoSum(self, nums, target):
        for i, data1 in enumerate(nums):
            for j, data2 in enumerate(nums):
                if i > j and (data1 + data2 == target):
                    return[i,j]