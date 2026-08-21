class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}
        for i in range(len(nums)):
            seeking = target - nums[i]
            if seeking in exist:
                return [exist[seeking], i]
            exist[nums[i]] = i
