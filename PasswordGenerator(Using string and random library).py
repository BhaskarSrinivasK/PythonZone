import random
import string
print('Wanna Generate Password')
length = int( input( '\nEnter the length of password required : '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all, length)
password = "".join(temp)
print(password)
print("Go! Go! Go! Use this secure one!!!")
