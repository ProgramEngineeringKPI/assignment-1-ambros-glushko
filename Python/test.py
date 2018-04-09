import main as lib

#parse all the info from csv
lib.get_data()

#here we get the rating of results
rating = lib.generate_rating(lib.students)
#now form a scholarship list
list = lib.get_scholarship(lib.all_students, rating)

#print the list to console
lib.form_output(list)
#and to a csv
lib.form_csv(list)
