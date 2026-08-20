class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            s = start + end

            if s == target:
                return [start +1, end -1]
            elif s < target:
                start += 1
            elif s> target:
                end -= 1
            