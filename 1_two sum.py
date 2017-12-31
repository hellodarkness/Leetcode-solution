//Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//You may assume that each input would have exactly one solution, and you may not use the same element twice.

//O(n)
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i

//O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        l=len(nums)-1
        if len(nums) <= 1:
            return False
        list = []
        for i in range(len(nums)):
            for l in range (i+1,len(nums)):
                if nums[i]+nums[l]==target:
                    return [i,l]
