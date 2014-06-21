#Assuming that class roster will be given in text file roster.txt in the same directory.

    class Student:

        def __init__(self, first, last, g1, g2, g3, g4, g5):
            self.first = first
            self.last = last
            self.grades = sorted([int(g1),int(g2),int(g3),int(g4),int(g5)])
            self.avg = self.average(self.grades)
    
        def average(self, list_of_grades):
            total = 0
            for grade in list_of_grades:
                total += int(grade)
            return total/len(list_of_grades)
    
        def __repr__(self):
            out = self.first + " " + self.last + " " 
            out += "("+ str(self.avg)+"%) " + "("+ determine_letter_grade(self.avg) + ")" + " "
            for grade in self.grades:
                out += str(grade) + " "
            return out
                
    
    def student_from_roster(given_line):
        data = given_line.split() # puts info into list form
        return Student (data[0].strip(','), data[1], data[2], data[3], data[4], data[5], data[6])
        
        
    def read_roster(filename):
        f = open(filename, 'r') #no need to be able to write file. 
        all_student_data = {}
        for line in f:
            all_student_data[student_from_roster(line)] = student_from_roster(line).average(student_from_roster(line).grades)
        f.close()
        return all_student_data
    
    def sort_roster(roster):
        return list(reversed(sorted(roster, key=lambda student:student.avg)))
    
    def output_roster(roster_list):
        """
        Accepts list of student data with each line looking like
        Andrew MacDougall 100 99 98 11 22
        and outputs a line like 
        Andrew MacDougall (66%) (B+) 11 22 98 99 100
        Returns all lines in a string.
        """
        out = ""
        for student in roster_list:
            out += student.__repr__() + "\n"
        return out
    
    def determine_letter_grade(numeric_grade):
        """
        Determines letter grade based on numeric grade. 
        Returns letter grade. 
        """
        rounded_numeric_grade = int(round(numeric_grade))
        if rounded_numeric_grade <= 59:
            letter_grade = 'F'
        elif rounded_numeric_grade >= 90:
            letter_grade = 'A' 
        elif rounded_numeric_grade >= 80 and rounded_numeric_grade <= 89:
            letter_grade = 'B' 
        elif rounded_numeric_grade >= 70 and rounded_numeric_grade <= 79:
            letter_grade = 'C' 
        else:
            letter_grade = 'D' 
        if letter_grade != 'F':
            last_digit = rounded_numeric_grade % 10
            if(last_digit <= 2):
                if (last_digit != 0 or letter_grade != 'A'):
                    letter_grade += '-'
            if(last_digit >=7 and letter_grade != 'A'):
                letter_grade += '+'
        return letter_grade
            
    
    
    
    if __name__ == "__main__":
        text_file = "roster.txt"
        print output_roster(sort_roster(read_roster(text_file)))
        
