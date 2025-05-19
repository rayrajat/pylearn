def division(a,b):
    return a//b , a/b

if __name__=="__main__":
    a = int(input())
    b = int(input())
    
    print(*division(a,b),sep="\n")
    