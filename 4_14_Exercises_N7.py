def computegrade(score1):
    if 0.9 <= score1 <= 1.0:
        grade1 = 'A'
    elif 0.8 <= score1 < 0.9:
        grade1 = 'B'
    elif 0.7 <= score1 < 0.8:
        grade1 = 'C'
    elif 0.6 <= score1 < 0.7:
        grade1 = 'D'
    elif 0.0 <= score1 < 0.6:
        grade1 = 'F'
    return grade1

score = input("Enter score: ")
grade = ''

try:
    score = float(score)
    if float(score) < 0 or float(score) > 1:
        print('Bad score')
    else:
        grade = computegrade(score)
        print(grade)
except:
    print('Bad score')
