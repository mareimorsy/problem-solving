class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums) // 3

        freq = {}
        result = []

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        for k, v in freq.items():
            if v > majority:
                result.append(k)

        return result