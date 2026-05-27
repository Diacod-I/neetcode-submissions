from heapq import nlargest
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        counts = Counter(nums)
        return nlargest(k, counts.keys(), key=counts.get)
        