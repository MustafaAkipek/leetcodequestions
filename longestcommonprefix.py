strs = ["flower","flow","flight"]

first = strs[0]
common = []
count = 0
last = []

for i in strs:
    for j in range(len(i)):
        common.append(i[j])
   
for i in common:     
    if common.count(i) == len(strs):
        last.append(i)
        
last = set(last)
lastl = []

print(last)