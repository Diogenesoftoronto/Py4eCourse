# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch
# it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.


# user creates a list of integers and stores value in an array
def int_list():
    ival = None
    i_array = []
    mival = input('Enter an Integer: ')
    if mival == 'done':
        print('You have not given values, yet you are done? Goodbye User. Enjoy life.')
        quit()
    try:
        mival = int(mival)
        print(mival)
        i_array.append(mival)
    except:
        print('Invalid input')
    while ival != 'done':
        ival = input('Enter an Integer: ')
        try:
            ival = int(ival)
            print(ival)
            i_array.append(ival)
        except:
            if ival == 'done':
                continue
            print('Invalid input')
            continue
    return i_array


i_array = int_list()
# find the index range of the returned value of the int_list () method/function or the range of any unknown array


# take list and find lowest number and largest number
for index, item in enumerate(i_array):
    if index == 0:
        low_num = i_array[index]
        high_num = i_array[index]
    elif i_array[index] > high_num:
        high_num = i_array[index]
    elif i_array[index] < low_num:
        low_num = i_array[index]
print('Maximum is', high_num)
print('Minimum is', low_num)
