class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        result = []

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j -=1
            elif sum < target:
                i +=1
            else:
                result = [i + 1, j+1]
                j -=1
                i +=1
        return result