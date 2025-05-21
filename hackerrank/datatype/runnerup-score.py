def Max(arr):
    current_max = arr[0]
    for i in arr:
        if i>current_max:
            current_max = i

    return current_max

def second_max(arr):
    maxima = Max(arr)

    second_List = [x for x in arr if x!=maxima]

    if second_List:
        max_value=Max(second_List)
        return max_value
    else:
        return None


if __name__=="__main__":
    n = int(input())
    List = list(set(map(int,input().split())))

    second_Max = second_max(List)

    if second_Max is not None:
        print(second_Max)
    else:
        print("second value not found")




    


    

    


    


    
    



