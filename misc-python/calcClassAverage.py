#!/usr/bin/env python -tt

"""jstephens - pyfu - 2014 july

Tool to help teachers calculate a class average
"""

## Define each student as a dictionary 
##        define keys as specific assingments
##        define values as the scores
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!

def average(listOfNumbers):
    runningTotal = 0
    for currentNum in listOfNumbers:
        runningTotal = runningTotal + currentNum
    averageScore = runningTotal / len(listOfNumbers)
    return averageScore
    

def get_average(studentDict):
    # homework = %10
    # quizzes = %30
    # tests = %60
    runningTotalWeightedScore = 0
    for keyAssignment in studentDict:
        if keyAssignment == "homework":
            homeworkWeightedAverage = average(studentDict[keyAssignment]) * .1
            runningTotalWeightedScore = runningTotalWeightedScore + homeworkWeightedAverage
        elif keyAssignment == "quizzes":
            quizzesWeightedAverage = average(studentDict[keyAssignment]) * .3
            runningTotalWeightedScore = runningTotalWeightedScore + quizzesWeightedAverage
        elif keyAssignment == "tests":
            testsWeightedAverage = average(studentDict[keyAssignment]) * .6
            runningTotalWeightedScore = runningTotalWeightedScore + testsWeightedAverage
    weightedAverageScore = runningTotalWeightedScore
    
    return weightedAverageScore
    
    
def get_letter_grade(score):
    if score >= 90:
        letterGrade = "A"
    if (score >= 80) and (score < 90):
        letterGrade = "B"
    if (score >= 70) and (score < 80):
        letterGrade = "C"
    if (score >= 60) and (score < 70):
        letterGrade = "D"
    if score < 60:
        letterGrade = "F"
    return letterGrade
    
def get_class_average(studentList):
    runningTotalToAverage = 0
    for studentName in studentList:
        studentAverage = get_average(studentName)
        runningTotalToAverage = runningTotalToAverage + studentAverage
    classAverage = runningTotalToAverage / len(studentList)
    return classAverage

listOfMyCurrentStudentDicts = [lloyd, alice, tyler]

classAverage = get_class_average(listOfMyCurrentStudentDicts)

print classAverage
        
        
        
