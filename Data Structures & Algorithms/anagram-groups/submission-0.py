from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            result["".join(sorted(string))].append(string)
        
        return [group for group in result.values()]