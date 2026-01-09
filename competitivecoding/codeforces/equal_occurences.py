#my solution
lst = list(map(int,input().split()))

# Step 1: Count elements
count_dict = {}
for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1

print("Initial dictionary:", count_dict)

values = list(count_dict.values())

# Step 2: Check if all values are equal
if len(set(values)) == 1:
    # All values equal
    result = []
    for k, v in count_dict.items():
        result.extend([k] * v)

    print("All values are equal")
    print("Length of list:", len(result))

else:
    # Step 3: Values are different
    # Find the value that most keys have (the common value)
    common_value = max(set(values), key=values.count)

    for key in count_dict:
        if count_dict[key] != common_value:
            count_dict[key] = common_value

    result = []
    for k, v in count_dict.items():
        result.extend([k] * v)

    #print("Values were different")
    #print("Updated dictionary:", count_dict)
    print("length of Result list:", len(result))

#actual solution

from collections import Counter
import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    a = [int(data[index + i]) for i in range(n)]
    index += n
    
    cnt = Counter(a)
    freq = sorted(cnt.values())
    
    ans = 0
    have = 0
    
    for f in reversed(freq):
        have += 1
        ans = max(ans, have * f)
    
    print(ans)



    