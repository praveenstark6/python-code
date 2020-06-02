# code for getting input in lowercase
string = str(input().strip().lower())
# the code for printing the length of the smallest substring with distinct characters.
l = []
for i in range(len(string)):
    if string[i] not in l:
        l.append(string[i])
m = 9999
for i in range(len(string)):
    l2 = [] + l[:]
    k = -1
    for j in range(i, len(string)):
        if string[j] in l2:
            l2.remove(string[j])
        if l2 == []:
            k = j
            break
    if k != -1:
        temp = k - i
        if temp < m:
            m = temp
print(m + 1)
# the code by Praveenkumar M