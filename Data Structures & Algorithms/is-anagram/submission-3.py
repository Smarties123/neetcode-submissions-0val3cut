class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapping = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
        
        for j in t:
            if j in mapping:
                mapping[j] -= 1
            else:
                return False
        
        for k in mapping:
            if mapping[k] != 0:
                return False

        return True
    

