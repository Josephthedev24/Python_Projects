class School:
    def __init__(self):
        self.students = []

    def add_student(self,id,name,surname,class_):
        '''
        This method allows us to add student to system.
        Id, name, surname, class are needed for this function.
        '''
        student = {
                'id':id,
                'name':name,
                'surname':surname,
                'class':class_,
                'exam_name':[],
                'exam_grade':[]
            }
        self.students.append(student)
        print(f'Student {name} added successfully')

    def add_grade(self,id,exam_name,exam_grade):
        '''
        This method allows us to add grade for specific student according to his/her id. 
        Exam name and exam grade can be added by this method
        '''
        for student in self.students:
            if student['id'] == id:
                student['exam_name'].append(exam_name)
                student['exam_grade'].append(exam_grade)
                print(f'Grades for ID:{id} is successfully added for {exam_name} exam as {exam_grade}')
                return
        print('Student not found.')

    def show_students(self):
        '''
        This method is used for display all the students with their info(id,name,surname,class,exam names and exam grades).
        '''
        for student in self.students:
            print(f'ID:{student['id']}, name:{student['name']}, surname:{student['surname']}, class:{student['class']}, exam_name:{student['exam_name']}, exam_grade:{student['exam_grade']}')
   
    def change_class(self,id,new_class):
        '''
        This function is for changing the class of the students.
        Id and new class parameters are required
        '''
        for student in self.students:
            if student['id'] == id:
                student['class'] = new_class
                print(f"Student {student['name']}'s class has been changed as {student['class']}")
                return
        print('Student not found.')

    def change_name(self,id,new_name):
        '''
        This function is for changing the name of the students.
        Id and new_name parameters are required
        '''
        for student in self.students:
            if student['id'] == id:
                student['name'] = new_name
                print(f"Student's name has been changed as {student['name']}")
                return
        print('Student not found.')

    def change_surname(self,id,new_surname):
        '''
        This function is for changing the surname of the students.
        Id and new_surname parameters are required
        '''
        for student in self.students:
            if student['id'] == id:
                student['surname'] = new_surname
                print(f"Student's name has been changed as {student['surname']}")
                return
        print('Student not found.')




