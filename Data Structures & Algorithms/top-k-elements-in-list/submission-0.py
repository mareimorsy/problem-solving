class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        arr = []
        for num, frequency in freq.items():
            arr.append([frequency, num])

        arr.sort()

        res = []

        for i in range(k):
            res.append(arr.pop()[1])
        return res