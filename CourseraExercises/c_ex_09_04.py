"""Name: c_ex_09_04.py
Description: This program takes a file and determines which email address sent the most amount of
email messages.

The program looks for 'From ' lines and takes the second word of those lines as the person
who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer"""
file_name = input('enter a file name: ')
file = open(file_name)
findstr = 'From '
email_names_list = list()
email_dict = dict()
for line in file:
    line_list = line.split()
    if line.startswith(findstr):
        email_names_list.append(line_list[1])
for email_name in email_names_list:
    email_dict.setdefault(email_name, 0)
    email_dict[email_name] += 1
freq_email_count = 0
freq_email_name = ''
for email_name, email_count in email_dict.items():
    if email_count > freq_email_count:
        freq_email_count = email_count
        freq_email_name = email_name
print(freq_email_name, freq_email_count)
