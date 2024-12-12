num = 123456

# Method 1:
rev = 0
while num > 0:
    reminder = num%10
    rev = rev * 10 + reminder
    num = num // 10

print(rev)

# Method 1:
num2=12345
print(str(num2)[::-1])
