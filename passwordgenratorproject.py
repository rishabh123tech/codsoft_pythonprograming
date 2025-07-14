
import random, string

n = int(input("Password length: "))           
if n < 2:
    raise ValueError("Length ≥ 2")


p = [random.choice(string.digits)]
p += [random.choice(string.ascii_letters + string.digits) for _ in range(n - 1)]
random.shuffle(p)                           
print(''.join(p))
