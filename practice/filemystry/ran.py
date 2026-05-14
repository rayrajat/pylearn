import random

# open file in write mode
with open("output.txt", "a") as f:
    for i in range(10):
        num = random.randint(1, 100)  # random number between 1 and 100
        f.write(str(num) + "\n")