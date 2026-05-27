from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        freqs = Counter(nums)
        return nlargest(k, freqs.keys(), key=freqs.get)
