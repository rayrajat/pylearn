#my solution
nums = [21, 4, 7]
total_sum = 0

for num in nums:
    divisors = []
    for j in range(1, num + 1):
        if num % j == 0:
            divisors.append(j)
    if len(divisors) == 4:
        total_sum += sum(divisors)
    else:
        print(0)

print(total_sum)


#actual solution
from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            divisors = set()
            for i in range(1, int(math.isqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                if len(divisors) > 4:  # Stop early if more than 4 divisors
                    break

            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum


