class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        print(closeToOpen)
        for symbol in s:
            if symbol in closeToOpen:
                if stack and stack[-1] == closeToOpen[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)

            
        if not stack:
            return True
        else:
            return False