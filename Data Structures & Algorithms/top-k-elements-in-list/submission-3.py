from heapq import nlargest
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        freqs = Counter(nums)
        return nlargest(k, freqs.keys(), key=freqs.get)
        