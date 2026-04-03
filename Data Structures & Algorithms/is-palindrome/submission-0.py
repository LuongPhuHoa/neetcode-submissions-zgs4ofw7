class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        counter_left = 0
        counter_right = 1
        while counter_left + counter_right < (n):
            if not s[counter_left].isalnum():
                counter_left += 1
                continue
    
            if not s[n-counter_right].isalnum():
                counter_right += 1
                continue

            if (s[counter_left].lower() != s[n-counter_right].lower()):
                return False

            counter_left +=1
            counter_right +=1
        
        return True
