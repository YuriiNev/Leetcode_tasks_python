"""Based on leetcode.com Task  194. Transpose File.

Given a text file file.txt, transpose its content.

You may assume that each field is separated by the ' ' character.
if there is no word you may put ' ' insted of it.
Punctuation marks are considered as a part of the word,
numbers are considered words.

Example:____________

If file.txt has the following content:

name age, date!
alice 21 of birth
ryan 30
Output the following:

name alice ryan
age, 21 30
date! of
  birth
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
Text_input_name = '194_words.txt'
Text_output_name = '194_result.txt'

i_p = Text_dir + Text_input_name  # input path
o_p = Text_dir + Text_output_name  # output path

file_i = open(i_p, 'r')  # Reading the file
file_o = open(o_p, 'w')  # Writing into the file

to_transpose = []  # the list for transposition
k = 0  # counter

""" the plan is to convert the line to a list of words
and then trnanspose the list of lists"""

line = file_i.readline()  # the zeroth line

""" we read line, split it into words,
add the list of words from the line into the list, which will be transposed"""
line_len_max = 0
while len(line) != 0:
    linelist = []  # list of words in line
    word = ''
    for i in range(len(line)):
        if line[i] == ' ' or line[i] == '\n':
            if word != '':  # empty words are not allowed
                linelist.append(word)
                word = ''
            # end if
        else:
            word += line[i]
        # end else
    # end for
    line_len = len(linelist)
    if line_len != 0:  # empty lines are not allowed
        to_transpose.append(linelist)
        if line_len > line_len_max:  # define the length of the longest line
            line_len_max = line_len
    # end if
    line = file_i.readline()
    k += 1
# end while


for i in range(line_len_max):
    transposed_line = ''
    for j in range(len(to_transpose)):
        if i < len(to_transpose[j]):
            transposed_line += to_transpose[j][i]
            transposed_line += ' '
        else:
            transposed_line += ' '  # space if there is no word
            transposed_line += ' '
        # end if
    # end for
    transposed_line += '\n'
    file_o.write(transposed_line)

file_o.close()
file_i.close()
