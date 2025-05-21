def Min(arr):
    current_min = arr[0]
    for i in arr:
        if i<current_min:
            current_min = i

    return current_min

def second_min(arr):
    minima = Min(arr)

    second_List = [x for x in arr if x!=minima]

    if second_List:
        min_value=Min(second_List)
        return min_value
    else:
        return None
if __name__=="__main__":

    n = int(input())

    student_marks = {}

    Marks_list  = []

    for i  in range(n):
        name = input()
        marks = float(input())

        student_marks[name] = marks

        Marks_list.append(marks)

second_lowgrade = second_min(Marks_list)

result_names = [name for name,marks in student_marks.items()if marks==second_lowgrade]

for name in sorted(result_names):
    print(name)



    



    

    

