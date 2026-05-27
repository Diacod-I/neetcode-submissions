class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            hashMap[''.join(sorted(s))].append(s)
            
        return list(hashMap.values())
        