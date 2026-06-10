class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        result = False
        recent_char = ""
        for char in s: 
            if char in "([{":
                stack.append(char)
                print(stack)
            if char == ")":
                if len(stack) > 0:
                    recent_char = stack.pop()
                    if recent_char == "(":
                        result = True
                    else: 
                        result = False
                        break
                else: 
                    stack.append(char)
            if char == "]":
                if len(stack) > 0:
                    recent_char = stack.pop()
                    if recent_char == "[":
                        result = True
                    else: 
                        result = False
                        break
                else: 
                    stack.append(char)   
            if char == "}":
                if len(stack) > 0:
                    recent_char = stack.pop()
                    if recent_char == "{":
                        result = True
                    else: 
                        result = False
                        break
                else: 
                    stack.append(char)
                   
        if len(stack) > 0: 
            result = False
        return result
