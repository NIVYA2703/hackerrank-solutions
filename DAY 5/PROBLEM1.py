def swap_case(s):
    answer = ""
    
    for ch in s:
        if ch.islower():
            answer+=ch.upper()
        elif ch.isupper():
            answer+=ch.lower()
        else:
            answer+=ch
            
    return answer
