

def above80(studentGrades, orderedStudentNames=[]):


    if not studentGrades:
        return orderedStudentNames, highThan80

    studentNames = min(studentGrades.keys())
    orderedStudentNames.append(studentNames)
    
    del studentGrades[studentNames]
    
    return above80(studentGrades, orderedStudentNames)
    
studentGrades={"Abram": 40, "Barry": 90, "Delta": 88, "Curt": 64, "Delta": 88}
highThan80 = {key:value for key, value in studentGrades.items() if value >80}

orderedStudentNames, highThan80 = above80(studentGrades.copy())

print(orderedStudentNames)
print(highThan80)
  
  
  
  