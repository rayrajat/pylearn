#my solution
class Solution:
    def reverse(self, x: int) -> int:
        n=abs(x)
        x1=(n%10) #3
        x3=(n//100) #1
        x2=((n//10)%10)#2
        reversed_num=x1*100+x2*10+x3
        return reversed_num if x > 0 else - + reversed_num
    
#actual solution

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
