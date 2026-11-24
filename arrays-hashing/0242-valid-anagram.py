class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}
        seen = 1
        for char in s:
            if char in set_s:
                set_s[char]= set_s[char] + 1
            else:
                set_s[char] = seen
        seen = 1
        for char in t:
            if char in set_t:
                set_t[char]= set_t[char] + 1
            else:
                set_t[char] = seen
        
        if set_s == set_t:
            print(set_t, set_s)
            return True
        else:
            return False
