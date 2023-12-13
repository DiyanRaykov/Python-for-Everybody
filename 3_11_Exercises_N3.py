score = input("Enter score: ")
grade = ''

try:
    score = float(score)
    if float(score) < 0 or float(score) > 1:
        print('Bad score')
except:
    print('Bad score')
    exit()

if 0.9 <= score <= 1.0:
    grade = 'A'
elif 0.8 <= score < 0.9:
    grade = 'B'
elif 0.7 <= score < 0.8:
    grade = 'C'
elif 0.6 <= score < 0.7:
    grade = 'D'
elif 0.0 <= score < 0.6:
    grade = 'F'

print(grade)
