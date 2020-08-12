

# This program should validate if the student successfuly passed the year
print('This program should validate if the student successfuly passed the year')
print('The student passed if: (gade1 + grade2)/2>=6 and the attendance rate is higher then 80%')

# ask for both grades 1 and 2
# ask for total num of classes
# ask for number of absences
# validate the inputs

#validate the grade input
data_validated = False
while(data_validated==False):
    grade_1 = input('Please provide the grade 1: ')
    try:
        grade_1 = float(grade_1)
    except:
        print('input should be int or float number separated with a dot')
        continue
    if(grade_1<0 or grade_1>10):
        print('The range for grade is from 0 to 10, please retry')
        continue
    else:
        data_validated = True
        
#validate the grade input
data_validated = False
while(data_validated==False):
    grade_2 = input('Please provide the grade 2: ')
    try:
        grade_2 = float(grade_2)
    except:
        print("input should be int or float number separated with a dot")
        continue
    if(grade_2<0 or grade_2>10):
        print('The range for grade is from 0 to 10, please retry')
        continue
    else:
        data_validated = True

#validate the total classes variable
data_validated=False
while(data_validated==False):
    total_classes = input('Please provide the total num of classes: ')
    try:
        total_classes = int(total_classes)
    except:
        print('The number of classes should be provided in integers')
    if(total_classes<1):
        print('The total number of classes should be more then 0')
        continue
    else:
        data_validated=True

# validate the absences variable
data_validated=False
while(data_validated==False):
    absences = input('Please provide the total num of absences: ')
    try:
        absences = int(absences)
    except:
        print("Please provide an integer value")
        continue
    if(absences>total_classes or absences<0):
        print("The num of absences can not be more then the num of attendance or less then 0, please retry ")
        continue
    else:
        data_validated=True

final_mark = (grade_1+grade_2)/2

attendance = (total_classes-absences)/total_classes
attendance_in_percent = attendance*100

print("Student's final mark is: {} ".format(final_mark))
print("The student's attendance is {}% ".format(round(attendance_in_percent, 2)))

if(final_mark>=6 and attendance>=0.8):
    print('The student have passed')
elif(final_mark<6):
    print('The final mark is too low, student failed')
elif(attendance<0.8):
    print('The attendance is too low, student failed')
else:
    print('nor final mark nor attendance is good, failed twicely..')

