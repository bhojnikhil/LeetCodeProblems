class Solution(object):
    def isValid(self, s):
        stack=[]
        match = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop() == match[ch]):#check if matching closing bracket exists!
                    return False #has no matching closing bracket
            else:
                stack.append(ch)
        return not stack #check if stack is empty