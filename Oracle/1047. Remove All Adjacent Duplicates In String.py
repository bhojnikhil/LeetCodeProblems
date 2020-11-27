class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for letter in S:
            
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)