import random

print("Want a Secure a password?")
length = int(input("Enter the length of password required!! : "))
lower = []
for i in range(65,91):
    lower.append(chr(i))
upper = []
for i in range(97,123):
    upper.append(chr(i))
symbols = []
for i in range(33,48):
    symbols.append(chr(i))
num = [0,1,2,3,4,5,6,7,8,9]
all = lower + upper + num + symbols
temp = random.sample(all, length)
password = ""
for i in range(length):
   password = password + str(temp[i])
print(password)
print("Go! Go! Go! Use this secure one!!!")
