
num = [1,2,3,5,6,8]

missing = []

for i in range(num[0],num[-1]):
    if i not in num:
        missing.append(i)

print(missing)