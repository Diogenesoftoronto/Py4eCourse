#Write a program that prompts for a file name, then opens that file and reads
#through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475|
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
file_Name = input("enter file name: ")
file = open(file_Name)
email_contents = file.read()
file.close()
email_contents_list = email_contents.split()
spam_con_list = []
float_spam_con = 0.000
str_spam_con = 'X-DSPAM-Confidence:'
"""here is a for loop that iterates over the range of a list index.
It then finds the index of a string in the list and adds the next string in the list to another list.
Then it removes that string from the original list. It loops until the end of the original list index."""
for file_index in range(len(email_contents_list)-1):
    try:
        file_index = email_contents_list.index(str_spam_con)
        spam_con_list.append(email_contents_list[file_index+1])
        email_contents_list.remove(str_spam_con)
    except:
        break
for element in spam_con_list:
    float_spam_con = float_spam_con + float(element)
float_spam_con = float_spam_con/float(len(spam_con_list))
print('Average spam confidence:',float_spam_con)
