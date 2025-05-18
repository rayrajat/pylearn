def calculate(a,b):
    return a+b,a-b,a*b
    
if __name__=="__main__":

    a = int(input())
    b = int(input())

    print(*calculate(a, b), sep='\n')
