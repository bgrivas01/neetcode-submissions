class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.replace(".", "")
        s = s.replace("?", "")
        s= s.replace(",", "")
        s = s.replace("'","")
        s = s.replace(":","")
        print(s)
        print(s[::-1])
        return s.lower() == s[::-1].lower()

    