#Write a Python program to count the number of lines in a file.

with open('lines.txt','w') as line:
    content = line.writelines('hey im your host and dost rajat standing riht here to enjoy and chill todaynight\n' 'and make this moment memorable')
    line.close()               

Count = 0

with open('lines.txt','r') as file:
    content = file.readlines()
    print(len(content))
    file.close()