"""
Name: c_ex_10_02.py
Description: Write a program to read through the mbox-short.txt and figure out the distribution by hour of
the day for each of the messages. You can pull the hour out from the 'From '
line by finding the time and then splitting the string a second time using a colon."""
find_str = 'From '
frequent_hours_dict = dict()
fname = input("enter a file: ")
file = open(fname)
# look at lines in file and enter lines that contain from into the line_list variable
line_list = [line.split() for line in file if line.startswith(find_str)]
# for each line of line_list split the line into a list of words and then enter that into
# a new list if the new list contains a colon
word_list = [[word for word in line if word.find(':') != -1] for line in line_list]
# split each time stamp into hours minutes and seconds
time_list = [[item.split(':') for item in elements] for elements in word_list]

# flattens lists that are nested


def flatten(nested_list):
    flattened_list = [item for sublist in nested_list for item in sublist]
    return flattened_list


# i think i can make this more elegant with a lambda or something.
time_list = flatten(time_list)
hours_list = [item[0] for item in time_list]
hours_list.sort()
# loop through each hour and add them to a dictionary with a default value of zero
# count how many times the same hour shows up in the list then print the hour and frequency that the hour appears
for hours in hours_list:
    frequent_hours_dict.setdefault(hours, 0)
    frequent_hours_dict[hours] = hours_list.count(hours)
# convert keys view method to a list
keys_list = list(frequent_hours_dict.keys())
# removes duplicate keys from dictionary
for keys in keys_list:
    for items in range(keys_list.count(keys)):
        if keys_list.count(keys) > 1:
            frequent_hours_dict.pop(keys)
        else:
            break
    print(keys, frequent_hours_dict[keys])
# c_ex_08_05.txt