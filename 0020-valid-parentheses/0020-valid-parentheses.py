class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = {')': '(',
        '}': '{',
        ']' : '['
        }

        stack_stored = []
        for brackets in s:
            if brackets in pattern:
                if not stack_stored:
                    return False
                if pattern[brackets] != stack_stored[-1]:
                    return False
                stack_stored.pop()
            else:
                stack_stored.append(brackets)
            # print(stack_stored)
        size = len(stack_stored)
        if size == 0:
            return True
        else:
            return False
