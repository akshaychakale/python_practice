num = 123456

rev = 0
while num > 0:
    reminder = num%10
    rev = rev * 10 + reminder
    num = num // 10

print(rev)

num2=12345
print(str(num2)[::-1])
