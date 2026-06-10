class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l,r = 0, len(new_s) - 1
        result = False

        if len(new_s) == 0: 
            result = True

        while l <= r: 
            if new_s[l] != new_s[r]: 
                result = False
                break 
            else: 
                result = True
                l += 1
                r -= 1
        print(l,r)
        return result