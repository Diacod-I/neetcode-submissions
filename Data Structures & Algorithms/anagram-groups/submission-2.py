class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            # retrieve sorted string as key and append string into anagram group
            hashMap[''.join(sorted(s))].append(s)

        return list(hashMap.values())
        