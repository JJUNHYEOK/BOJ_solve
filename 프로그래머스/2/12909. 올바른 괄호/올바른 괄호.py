def solution(s):
    stk = []
    
    for char in s:
        if char == '(':
            stk.append(char)
            
        else:
            if not stk:
                return False
            
            stk.pop()
            
    return len(stk) == 0