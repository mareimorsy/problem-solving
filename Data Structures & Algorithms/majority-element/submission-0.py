class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        major = nums[0]

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[major] < freq[i]:
                major = i
        return major