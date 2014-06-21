"""
#Description:

It is that time of year again. The Intro to Computer Science 101 class has ended at Greendale community college and the professor has to submit the final grades. The school requires grades to be submitted with a letter grade. In addition the grades should be submitted from the "best" student first. The individual scores should be be listed from "worse" to "best".

#Input:

You will be given class roster in the form of:

    (first name) , (last name) (score 1) (score 2) (score 3) (score 4) (score 5)

#Data Crunch:

Each student has 5 scores from 1 to 100. So a total of 500 points for the class.
Based on this you must determine what grade they get on a percentile 1-100. 

The letter Grades are assigned based on the following

* 90-100 A
* 80-89 B
* 70-79 C
* 60-69 D
* 59 and below F

Those scoring in the top 3 percent of the rank get a "+" added. Those scoring in the lower 3 percent of the rank get a "-". However there is no "+" for an A and there are no "+" or "-" for an F grade.

    student scoring 82% would be a B-
    student scoring 79% would be a C+


Note: Final Grades are rounded to the nearest whole number. So 89.5 is 90 and 89.4 is 89.

#Output:

The output should be ranked from the "best" student who had the best grade to the "worse" student who had the lowest grade. The 5 scores should also be arranged from the "lowest" to "highest".


The output should take on this form:

    (Last Name) (First Name) (Final percentage) (Final Grade) : (Scores 1-5 from low to high)

Example:

    Valerie	Vetter 79	81	78	83	80
    Richie	Rich	88	90	87	91	86

Would output as:

    Rich    Richie  (88%) (B+): 86 87 88 90 91
    Valerie Vetter (80%) (B-): 78 79 80 81 83 

#Formatting:

Optional but keep in mind the dean of the college is going to be looking at this and it might be fun and a good idea to align the output to make it look nice and easy to read.

#Challenge input:

    Jennifer ,	Adams	100	70	85	86	79
    Bubba ,	Bo Bob	50	55	60	53	30
    Matt ,	Brown	72	82	92	88	79
    Ned ,	Bundy	73	75	80	79	88
    Alfred ,	Butler	80	90	70	100	60
    Sarah ,	Cortez	90	72	61	70	80
    William ,	Fence	88	86	83	70	79
    Casper ,	Ghost	80	85	87	89	90
    Opie ,	Griffith	90	90	90	90	90
    Tony ,	Hawk	60	60	60	72	72
    Kirstin ,	Hill	100	90	92	94	95
    Hodor ,	Hodor	40	50	53	62	33
    Clark ,	Kent	89	90	88	92	91
    Tyrion ,	Lannister	93	97	100	91	95
    Ken ,	Larson	70	80	85	73	79
    Stannis ,	Mannis	60	70	75	77	78
    Bob ,	Martinez	79	88	92	82	72
    Jean Luc ,	Picard	90	89	95	70	65
    Harry ,	Potter	73	75	77	69	73
    Jaina ,	Proudmoore	90	92	100	95	94
    Richie ,	Rich	88	90	87	91	86
    John ,	Smith	90	80	70	60	50
    Jon ,	Snow	70	70	70	70	72
    Arya ,	Stark	91	92	90	93	90
    Edwin ,	Van Clef	40	50	55	57	33
    Valerie ,	Vetter	79	81	78	83	80
    Katelyn ,	Weekes	90	95	92	93	97
    Wil	 , Wheaton	70	80	75	71	77
    Steve ,	Wozniak	88	89	87	86	85
    Derek ,	Zoolander	80	81	85	88	90
"""

#Assuming that class roster will be given in text file roster.txt in the same directory.


class Student:
    """
    Hold the data for a student all in one place.
    """
    def __init__(self, first, last, g1, g2, g3, g4, g5):
        self.first = first
        self.last = last
        # cast grades to int so that sort works properly.
        self.grades = sorted([int(g1),int(g2),int(g3),int(g4),int(g5)])
        self.avg = self.average(self.grades)

    def average(self, list_of_grades):
        total = 0
        for grade in list_of_grades:
            total += int(grade)
        return total/len(list_of_grades)

    # Put in __repr__ for formatting later.
    def __repr__(self):
        out = self.first + " " + self.last + " " 
        out += "("+ str(self.avg)+"%) " + "("+ determine_letter_grade(self.avg) + ")" + " "
        for grade in self.grades:
            out += str(grade) + " "
        return out
            

def student_from_roster(given_line):
    """
    Creates a student from a line of the given roster (passed as given_line)
    Remember that given_line will be of the form 
    (first name) , (last name) (score 1) (score 2) (score 3) (score 4) (score 5)
    brackets not actually included in the input, i.e.
    Andrew, MacDougall 100 98 98 33 44
    Returns a student object representing this line.
    """
    data = given_line.split() # puts info into list form
    return Student (data[0].strip(','), data[1], data[2], data[3], data[4], data[5], data[6])
    
    
def read_roster(filename):
    """
    Reads in the lines of text file filename as students and puts each student object in a dictionary, with the key being the repr
    of the student and the value being the student's average.
    Returns this list at the end. 
    """
    f = open(filename, 'r') #no need to be able to write file. 
    all_student_data = {}
    for line in f:
        all_student_data[student_from_roster(line)] = student_from_roster(line).average(student_from_roster(line).grades)
    f.close()
    return all_student_data

def sort_roster(roster):
    """ 
    Sorts roster based on average grade. 
    Returns ordered list of students, from highest to lowest.
    """
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
