class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashSet = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if hashSet[temp]:
                return [hashSet[temp], i + 1]
            hashSet[numbers[i]] = i + 1
        return []
        