class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}

        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
            
        for j in t:
            if j not in s_dict:
                return False
            if j in s_dict:
                s_dict[j] -= 1
        
        for k in s_dict:
            if s_dict[k] != 0:
                return False
        
        return True