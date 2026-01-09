lst=[1, 4, 2, 10, 23, 3, 1, 0, 20],
k=4
Sum=[]
for i in range(len(lst)-1):
    temp=[i for i in range(k-1)]
    Sum.append(sum(temp))

    print(Sum)
