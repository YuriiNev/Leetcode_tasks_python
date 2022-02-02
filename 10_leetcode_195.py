"""Based on leetcode.com Task  195. Nth Line.

Given a text file file.txt, print just the 10th line of the file.

Example:_______________

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:

Line 10
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
Text_input_name = '195_lines.txt'
Text_output_name = '195_result.txt'

i_p = Text_dir + Text_input_name  # input path
o_p = Text_dir + Text_output_name  # output path

file_i = open(i_p, 'r')  # Reading the file
file_o = open(o_p, 'w')  # Writing into the file

N = 15  # the number of the printed line
for i in range(N):
    line = file_i.readline()
file_o.write(line)

file_o.close()
file_i.close()
