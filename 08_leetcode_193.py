"""Based on the leetcode.com Task  Task 193. Valid Phone Numbers.

Given a text file phone.txt that contains a text with phone numbers
, write a script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the
following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

Example:________________________________________________________________

Assume that file.txt has the following content:

1-987-123-4567
abc
  123 456 7890  cdr

(123) 456-7890
234-567-890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
234-567-890
"""

"""
FILES STRUCTURE:

Sqlite_querry_functions package is located in Additional_functions folder
(sqlite_querry_functions package);

Input and output databases are located in Databases folder;

Text filies inputs and outputs are located in Text_files folder

Databases names are the same as in the tasks but
with the number of task in the end, such as Person_175, Address_175 etc.

names of files others then databases have built on a principle that the
number stays in fron of the name, i.e. 192_words.txt or 192_result.txt.
"""

"""=================
  DEFINITION SECTION
================="""

# please, check the existance of the following folder and files
Text_dir = 'Text_files/'
Text_input_name = '193_phones.txt'
Text_output_name = '193_result.txt'

i_p = Text_dir + Text_input_name  # input path
o_p = Text_dir + Text_output_name  # output path

file_i = open(i_p, 'r')  # Reading the file
file_o = open(o_p, 'w')  # Writing into the file

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

numbers = []  # the list of numbers
number = ''  # parameter for saving current number
type1 = False  # flag for the numbers of the first type
type2 = False  # flag for the numbers of the second type
k = 0  # counts quantity of symbols in a number

""" line = file_i.readline()  # reading a line """
file_text = file_i.read()
for sym in file_text:
    """checking for phone number type 1: (123) 456-7890"""
    # START
    if sym == '(':
        number += sym
        type1 = True

    # condition and counter-condition
    if type1 is True and k < 4 and sym != '(':
        if sym in digits:
            number += sym
        else:
            number = ''
            type1 = False
            k = 0

    # condition and counter-condition
    if type1 is True and k == 4:
        if sym == ')':
            number += sym
        else:
            number = ''
            type1 = False
            k = 0

    # condition and counter-condition
    if type1 is True and k == 5:
        if sym == ' ':
            number += sym
        else:
            number = ''
            type1 = False
            k = 0

    # condition and counter-condition
    if type1 is True and k < 9 and k > 5:
        if sym in digits:
            number += sym
        else:
            number = ''
            type1 = False
            k = 0

    # condition and counter-condition
    if type1 is True and k == 9:
        if sym == '-':
            number += sym
        else:
            number = ''
            type1 = False
            k = 0

    # condition and counter-condition
    if type1 is True and k < 14 and k > 9:
        if sym in digits:
            number += sym
        else:
            number = ''
            type1 = False
            k = 0

    # increasing k
    if type1 is True:
        k += 1
    # FINISH
        if k == 14:
            numbers.append(number)
            k = 0
            number = ''
            type1 = False

    """checking for phone number type 2: 987-123-4567"""

    # START
    if sym in digits and k == 0:
        number += sym
        type2 = True

    # condition and counter-condition
    if type2 is True and k < 3 and k > 0:
        if sym in digits:
            number += sym
        else:
            number = ''
            type2 = False
            k = 0

    # condition and counter-condition
    if type2 is True and k == 3:
        if sym == '-':
            number += sym
        else:
            number = ''
            type2 = False
            k = 0

    # condition and counter-condition
    if type2 is True and k > 3 and k < 7:
        if sym in digits:
            number += sym
        else:
            number = ''
            type2 = False
            k = 0

    # condition and counter-condition
    if type2 is True and k == 7:
        if sym == '-':
            number += sym
        else:
            number = ''
            type2 = False
            k = 0

    # condition and counter-condition
    if type2 is True and k > 7 and k < 12:
        if sym in digits:
            number += sym
        else:
            number = ''
            type2 = False
            k = 0

    # increasing k
    if type2 is True:
        k += 1
    # FINISH
        if k == 12:
            numbers.append(number)
            k = 0
            number = ''
            type2 = False


for i in range(len(numbers)):
    file_o.write(numbers[i] + '\n')

file_o.close()
file_i.close()
