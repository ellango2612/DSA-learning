'''
Valid Parentheses
 
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
'''

## remember, the stack must be empty after we pop the last item for the string to be valid

class Solution:
    def isValid(self, s):
        hash_map = {'{':'}', '(':')', '[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in hash_map:
                stack.append(s[i]) # stack = [[]
            elif stack and s[i] in hash_map.values() and hash_map[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
        return not stack