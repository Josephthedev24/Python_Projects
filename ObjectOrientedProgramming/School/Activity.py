from Students import School




ExampleSchool = School()

#Adding Students
ExampleSchool.add_student(1,'John','Doe','Uni-3')
ExampleSchool.add_student(2,'Michael','Jordan','Uni-2')
ExampleSchool.add_student(3,'Emily','Dann','Uni-1')


#Adding Grades
ExampleSchool.add_grade(1,'Math',100)
ExampleSchool.add_grade(1,'Science',95)
ExampleSchool.add_grade(2,'Math',90)
ExampleSchool.add_grade(3,'Literature',85)
ExampleSchool.add_grade(3,'Math',100)

#Changing class_
ExampleSchool.change_class(1,'Uni-2')
ExampleSchool.change_class(2,'Uni-3')

#Changing name
ExampleSchool.change_name(1,'Josh')
ExampleSchool.change_name(3,'Mary')

#Changing surname
ExampleSchool.change_surname(2,'Bryant')
ExampleSchool.change_surname(1,'Krann')

#Display students
ExampleSchool.show_students()


