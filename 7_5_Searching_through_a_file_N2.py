fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()  # премахва бялото поле в дясно, вкл. \n и така премахва празните редове
    if line.startswith('From:'):
        print(line)