
def find_(num):
    missing_number = []
    low = min(num)
    high = max(num)
    for i in range(low,high+1):
        if not(i in num):
            missing_number.append(i)
    
    return missing_number



numbers = [1,2,5,6]
answer = find_(numbers)
print(answer)