import random

f = open("input.txt", "w")
for i in range(10):
    rand = random.randint(0, 1000000)
    f.write(str(rand))
    f.write("\n")
f.close()

