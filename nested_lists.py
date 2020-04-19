if __name__ == '__main__':
    list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=[score,name]
        list.append(student)
    list = sorted(list)    
    #print(list)    
    low_grade = list[0][0]
    students_with_second_grade =[]
    second_grade = -1
    for element in list:
        if (element[0]>low_grade and second_grade == -1):
            second_grade = element[0]
            #print("Second grade",second_grade)
        if (second_grade == element[0]):
            students_with_second_grade.append(element[1])
        elif (second_grade > -1):
            break    
    for st in sorted(students_with_second_grade):
        print(st)
