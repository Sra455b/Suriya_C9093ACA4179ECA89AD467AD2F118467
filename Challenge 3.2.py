class Student:
    def __init__(self, name, roll_number, cgpa):
      self.name=name
      self.roll_number=roll_number
      self.cgpa=cgpa

def sort_students(student_list):

  sorted_students = sorted(student_list,
                          key =lambda student:student.cgpa,reverse=True)
  return sorted_students
    
    
students = [
    Student("suriya","cb45",10.0),
    Student("abhishek","cb46",9.9),
    Student("yogesh","cb47",9.5),
    Student("sanjay","cb48",8.5)]


sorted_students=sort_students(students)
   
   
for student in sorted_students:
    print("Name: {},Roll Number: {},CGPA: {}".format(student.name, student.roll_number,student.cgpa))
   
   

 
    
    
    


 