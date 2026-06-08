from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)
        tMap = defaultdict(int)
        if len(s) != len(t):
            return False
        else:
            for i,j in zip(s,t):
                sMap[i] += 1
                tMap[j] += 1
            
            for i in sMap.keys():
                if i not in tMap:
                    return False
                elif tMap[i] != sMap[i]:
                    return False
                
        return True