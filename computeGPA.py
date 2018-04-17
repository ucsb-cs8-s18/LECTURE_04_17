

grades = {
    "courses" : [  
        {"course":"CMPSC 8", "units":4,"grade":"A"},
        {"course":"MATH 3A", "units":4,"grade":"B+"},
        {"course":"WRIT 2", "units":4,"grade":"B-"}
    ]
}




lg2Num = { 'A' : 4.0, 'A-':3.7,
           'B+' : 3.3, 'B': 3.0, 'B-': 2.7,
           'C+' : 2.3, 'C': 2.0, 'C-': 1.7,
           'D+' : 1.3, 'D': 1.0, 'D-': 0.7,
           'F': 0.0 }


def totalUnits(grd):
    " grd: grade report dictionary. return total units "

    # Pull out the list of courses
    listOfCourses = grd["courses"]

    totalUnits = 0
    for course in listOfCourses:
        totalUnits = totalUnits + course['units']
    return totalUnits

def totalPoints(grd):
    " grd: grade report dictionary. return total units "
    # Pull out the list of courses
    listOfCourses = grd["courses"]

    totalPoints = 0
    for course in listOfCourses:
        totalPoints = totalPoints + (course['units'] * lg2Num[ course['grade'] ] )
        # totalPoints = totalPoints + (course['units'] * letterGradeToNumber( course['grade'] ))
    return totalPoints    

def gpa(student):
    return  totalPoints(student)/totalUnits(student)

def letterGradeToNumber(letter):
    if letter=='A':
        return 4.0
    if letter == 'A-':
        return 3.7
    if letter == 'B+':
        return 3.3
    if letter == 'B':
        return 3.0
    if letter == 'B-':
        return 2.7
    if letter == 'C+':
        return 2.3
    if letter == 'C':
        return 2.0
    if letter == 'C-':
        return 1.7
    if letter == 'D+':
        return 1.3
    if letter == 'D':
        return 1.0
    if letter == 'D-':
        return 0.7
    else:
        return 0


student1 = {
    "courses" : [  
        {"course":"CMPSC 8", "units":4,"grade":"A"},
        {"course":"MATH 3A", "units":4,"grade":"B+"},
        {"course":"WRIT 2", "units":4,"grade":"B-"}
    ]
}

student2 = {
    "courses" : [  
        {"course":"MATH 8", "units":5,"grade":"D"},
        {"course":"CMPSC 16", "units":4,"grade":"B+"},
        {"course":"WRIT 2", "units":4,"grade":"B-"}
    ]
}

# Let the record reflect---these fictional grades were shouted out
# by students in the class.  They do not necessarily reflect
# on my opinions.

student3 = {
    "courses" : [  
        {"course":"MATH 8", "units":5,"grade":"C"},
        {"course":"CMPSC 16", "units":4,"grade":"B+"},
        {"course":"WRIT 2", "units":4,"grade":"B-"},
        {"course":"PSTAT 10","units":5,"grade":"F"}
    ]
}

def test_totalunits_1():
    assert totalUnits(student1)==12
    
def test_totalunits_2():
    assert totalUnits(student2)==13

def test_totalunits_3():
    assert totalUnits(student3)==18

def test_totalpoints_1():
    assert totalPoints(student1)==40
    
def test_totalpoints_2():
    assert totalPoints(student2)==29

def test_totalpoints_3():
    assert totalPoints(student3)==34



def test_gpa_1():
    assert gpa(student1)==40/12
    
def test_gpa_2():
    assert gpa(student2)==29/13

def test_gpa_3():
    assert gpa(student3)==34/18

    
