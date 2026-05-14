"""ord() — "ordinal"
ord(char) returns the Unicode (ASCII) code of a character.

✅ Example:
python
Copy
Edit
ord('A')   # ➝ 65
ord('a')   # ➝ 97
ord('0')   # ➝ 48"""

'''chr() — "character"
chr(code) takes a number (ASCII/Unicode code) and returns the character.

✅ Example:
python
Copy
Edit
chr(65)   # ➝ 'A'
chr(97)   # ➝ 'a'
chr(48)   # ➝ '0' '''

""" repr() gives the string representation of the value, including quotes for strings."""


'''abs()=The absolute value of a number is its distance from 0 on the number line — without considering the sign.

So:

abs(5) → 5

abs(-5) → 5

abs(0) → 0

✅ Usage Examples:
python
Copy
Edit
print(abs(10))     # ➝ 10
print(abs(-10))    # ➝ 10
print(abs(0))      # ➝ 0
print(abs(-3.5))   # ➝ 3.5
Works on both integers and floats!

🧠 Real Life Analogy:
If someone says “I’m 3 km away from the office,” it doesn’t matter if they’re north or south, the distance is still 3 km — that’s absolute value.

🔧 In Code Logic:
We often use abs() to:

Make sure numbers are positive before processing

Compare distances

Calculate differences (like abs(a - b))'''



# to convert int to string but now this does in range(0-9)
def convert(x):
    if x == 0:
        return '0'
    elif x > 0:
        y = chr(ord('0') + x)
        return type(y), y
    elif x < 0:
        y = '-' + chr(ord('0') + (-x))
        return type(y), y
    else:
        return "Invalid number"
    
def bigconvert(x):
    if x == 0:
        return '0'
    
    negative = x < 0
    x = abs(x)
    result = ''
    
    while x > 0:
        digit = x % 10
        result = chr(ord('0') + digit) + result
        x //= 10

    return '-' + result if negative else result

    


def convert(x):
    if x == 0:
        return '0'
    elif x > 0:
        y = chr(ord('0') + x)
        return type(y), y
    elif x < 0:
        y = '-' + chr(ord('0') + (-x))
        return type(y), y
    else:
        return "Invalid number"
    
def bigconvert(x):
    if x == 0:
        return '0'
    
    negative = x < 0
    x = abs(x)
    result = ''
    
    while x > 0:
        digit = x % 10
        result = chr(ord('0') + digit) + result
        x //= 10

    return '-' + result if negative else result

    


if __name__=="__main__":
    x=int(input("enter integer:"))
    if x in range(-9,10):
        print(convert(x))
    else:
        print(bigconvert(x))

    



