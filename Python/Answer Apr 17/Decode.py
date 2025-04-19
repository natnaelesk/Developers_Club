

def solv(item):
    stack = []
    num = 0
    cur_str = ''

    for i in item:
        if i.isdigit():
            num = num * 10 + int(i)
        elif i == "[":
            stack.append((cur_str,num))
            num = 0
            cur_str = ""
        elif i == "]":
            prev_str , prev_num = stack.pop()
            cur_str = prev_str + cur_str * prev_num
        else:
            cur_str = cur_str + i 
        
    return cur_str


print(solv("2[ab3[c]]"))
