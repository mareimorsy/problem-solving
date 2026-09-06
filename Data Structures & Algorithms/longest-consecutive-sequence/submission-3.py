class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        
        longest = 1
        sequence = 1

        nums.sort()

        for i in range (1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                sequence +=1
                longest = max(sequence, longest)
            else:
                sequence = 1
        return longest
                