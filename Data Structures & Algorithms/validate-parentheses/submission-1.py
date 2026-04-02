class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ['(','[',"{"]
        closed_list = [')',']','}']
        stack= []
        i=0
        while i < len(s):
            if s[i] in open_list:
                stack.append(s[i])
            else:
                closed_index = closed_list.index(s[i])
                if stack:
                    if stack[-1] != open_list[closed_index]:
                        return False
                    stack.pop()
                else:
                    return False
            i += 1
        return len(stack)==0