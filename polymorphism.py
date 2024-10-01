class Student:
    def calculate_percentage(self, total_marks):
        pass  


class Grade5Student(Student):
    def calculate_percentage(self, total_marks):
        subjects = 5
        return total_marks / (subjects * 100) * 100


class Grade10Student(Student):
    def calculate_percentage(self, total_marks):
        subjects = 6
        return total_marks / (subjects * 100) * 100


class Grade12Student(Student):
    def calculate_percentage(self, total_marks):
        subjects = 7  
        return total_marks / (subjects * 100) * 100


def main():
    
    grade5_student = Grade5Student()
    grade10_student = Grade10Student()
    grade12_student = Grade12Student()
    
    total_marks_grade5 = 400  
    total_marks_grade10 = 480  
    total_marks_grade12 = 600  


    print("Grade 5 Percentage: ",grade5_student.calculate_percentage(total_marks_grade5))
    print("Grade 10 Percentage: ",grade10_student.calculate_percentage(total_marks_grade10))
    print("Grade 12 Percentage: ",grade12_student.calculate_percentage(total_marks_grade12))


if __name__ == "__main__":
    main()