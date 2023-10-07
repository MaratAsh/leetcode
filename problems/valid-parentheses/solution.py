class Solution(object):
    PARENTHESES = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    def isValid(self, s):
        stack = list()
        for symbol in s:
            if symbol in Solution.PARENTHESES:
                stack.append(symbol)
            elif len(stack) > 0:
                last_sym = stack.pop()
                if Solution.PARENTHESES[last_sym] != symbol:
                    return False
            else:
                return False
        return not len(stack)
