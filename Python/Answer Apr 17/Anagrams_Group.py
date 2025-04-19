list_ =   ["eat", "tea", "tan", "ate", "nat", "bat"]
output = []

i=0
while i < len(list_):
    val = sorted(list_[i])
    grp = []
    j = i 
    while j < len(list_):
        if val == sorted(list_[j]):
            grp.append(list_[j])
            list_.pop(j)
            continue
        j += 1
    output.append(grp)

print(output)

        