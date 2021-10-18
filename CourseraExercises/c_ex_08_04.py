""""Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to see if the word is
already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order."""
fname = input("enter file name: ")                    
with open(fname) as file:                             
    fcontents = file.read()                           
fcontents_list = fcontents.split()                    
for word in fcontents_list:                           
    num_instances = fcontents_list.count(word)
    #if num_instances == 0:
        #fcontents_list.append(word)
    while num_instances > 1:                          
        fcontents_list.pop(fcontents_list.index(word))
        num_instances -= 1                            
print(sorted(fcontents_list))                         