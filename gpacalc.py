def grader(score: float):
    """ determines the grade and grade point of a score"""
    score = float(score)
    if score > 100:
        raise ValueError('Score can\'t be above 100!')
    elif score >= 70:
        grade, grade_point = 'A', 5
    elif score >= 60 and score <= 69:
        grade, grade_point = 'B', 4
    elif score >= 50 and score <= 59:
        grade, grade_point = 'C', 3
    elif score >= 45 and score <= 49:
        grade, grade_point = 'D', 2
    elif score >= 40 and score <= 44:
        grade, grade_point = 'E', 1
    elif score <= 39:
        grade, grade_point = 'F', 0
    return grade, grade_point


def gpaCalc(dict_of_results: dict):
    """
        computes the gpa of student and the dict_of_results
        is updated with more info
        dict_of_results takes this format
        dict_of_results = {course_code: [unit, score]}
        tnu = Total No. of Units
        tcp = Total Credit Points
    """
    tnu, tcp = 0, 0
    for course_code, list_of_info in dict_of_results.items():
        unit: int = list_of_info[0]
        score: int = list_of_info[1]
        grade = grader(score)[0]
        grade_point = grader(score)[1]
        credit_point = grade_point * unit
        dict_of_results[course_code].append((grade, grade_point, credit_point))
        tnu += unit
        tcp += credit_point
    gpa = tcp/tnu
    #since gpa is rounded accurately to 2 d.p
    return round(gpa, 2)

#test code
dude_results = {'MTH101': [4, 56],'CHM101': [5, 65],'PHY101': [3, 59],'CSC101': [1, 47]}
print(f'Your GPA is: {gpaCalc(dude_results)}')
