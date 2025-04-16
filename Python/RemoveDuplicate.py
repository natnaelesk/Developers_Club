nums = [1,2,3,4,5,5,6,2,3,7,8,1]
dic = {}

for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

clear_list = []
for j in dic.keys():
    if dic[j] == 1:
        clear_list.append(j)


print(clear_list)

