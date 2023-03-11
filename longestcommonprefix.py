strs = ["flower","flow","flight"]

first = strs[0]
common = []
count = 0
last = []

for i in range(len(strs)):
    if len(strs[i]) < len(first):
        min = len(strs[i])

for i in strs:
    for j in range(min):
        common.append(i[j])
   
for i in common:     
    if common.count(i) == len(strs):
        last.append(i)
        
last = set(last)
lastl = []

for i in last:
    lastl.append(i)
    
print(lastl)
    