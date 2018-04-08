import math

#initialize some global variables
#This list contains all the data about students you need
print('Frame connected successfully...')
students = []
student_marks = []
all_students = 0

#parse csv in 2-dim array
def get_data():
  global students
  input_file = open(input("Enter the file name: ") + ".csv", 'r')

  for element in input_file:
    student_info = element.split(",")
    students.append(student_info)


#generate rating and return it in a dictionary form
def generate_rating(group):
  students_rating = {}
  global all_students

  group.pop(0)
  data = []
  for i in group:
    if i[6][:-1] == "FALSE":
      data.append(i)
  group = data
  all_students = len(group)

  print('Ratings generation started...')
  for i in group:
    name = i[0]
    mark = (int(i[1]) + int(i[2]) + int(i[3]) + int(i[4]) + int(i[5])) / 5.000
    mark = format(mark, '.3f')
    if name in students_rating:
      if (students_rating[name] < mark):
        students_rating[name] = mark
    else:
      students_rating[name] = mark

  return students_rating


#count an amount of scholarships based on rating
def get_scholarship(all_students, rating):
  all_scholarships = math.floor(all_students * 0.4)

  rating = sorted(rating.items(), key=lambda x: x[1])
  rating.reverse()
  print('The rating is sorted...')

  scholars = rating[:all_scholarships]
  print('We got the scholarships...')

  return scholars


#print everything to a console in a fancy form
def form_output(result):
  print('Preparing the results... \n\n')
  for i in result:
    print(i[0] + " - " + i[1])
  print("\n\n\nМінімальний бал: " + str(result[len(result)-1][1]))

#export everything to a CSV in a fancy form
def form_csv(result):
  output_file = open(input('\n\nName the file: ') + '.csv', 'w')

  for i in result:
    output_file.write(i[0] + ' - ' + i[1] + '\n')

  output_file.write("\n\n\nМінімальний бал: " + str(result[len(result) - 1][1]))

  output_file.close()
  print('\n\nSuccessfully exported into CSV...')

