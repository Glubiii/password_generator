# simple password generator

import random

lower = 'qwertyuiopasdfghjklçzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
number = '1234567890'
symbol = '!@#$%&*?'

total = lower + upper + number + symbol

length = int(input('enter password length : '))
senha = ''.join(random.choices(total, k=length))

print(f'your password is : {senha}')
