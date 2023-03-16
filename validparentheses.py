def gek(s):
    values = {
            "(" : 1,
            ")" : -1,
            "{" : 2,
            "}" : -2,
            "[" : -3,
            "]" : 3
        }

    result = 0
    same = 0

    for i in range(len(s)):
        result += values[s[i]]
    
    for i in range(0, len(s), 2):
        if i+1 < len(s) and values[s[i]] + values[s[i+1]] == 0:
            same += 1
        
    
    if result == 0 and same == len(s) / 2:
        return True

    else:
        return False
    
print(gek("{[]}"))