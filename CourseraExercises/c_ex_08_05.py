"""Name:c_ex_08_05.py
Description: Python coursera course exercise number 8.5.
This program takes a file and prints the number of email addresses
in the file along with the email addresses that appear in the email."""
fname = input('enter file name: ')
file = open(fname)
count = 0
findstr = 'From '
for line in file:
    line.rstrip()
    if line.startswith(findstr):
        file_list = line.split()
        count += 1
        print(file_list[1])
print(f'There were {count} lines in the file with {findstr}as the first word')