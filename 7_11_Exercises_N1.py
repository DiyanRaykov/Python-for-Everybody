# fh = input("Enter a file name: ")
# try:
#     fh = open(fh)
# except:
#     print("File cannot be opened:")
#     exit()

fh = open("mbox-short.txt")

for lx in fh:
    line = lx.rstrip()
    # if line.find('5 09:14:16 2008') == -1: continue
    print(line.upper())


# find_str = f_open
# print(fh)


