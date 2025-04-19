
def even_total(num):
    total = 0
    for i in num:
        if i % 2==0:
            total+= i
    return total


numbers = [1,2,3,4,5,6,7,8,9]
answer = even_total(numbers)
print(answer)