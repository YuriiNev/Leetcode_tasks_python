"""Based on leetcode.com Task  194. Transpose File.

Given a text file file.txt, transpose its content.

You may assume that each field is separated by the ' ' character.
if there is no word you may put ' ' insted of it

Example:____________

If file.txt has the following content:

name age date
alice 21 of birth
ryan 30
Output the following:

name alice ryan
age 21 30
date of
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
Text_input_name = '193_phones.txt'
Text_output_name = '193_result.txt'

i_p = Text_dir + Text_input_name  # input path
o_p = Text_dir + Text_output_name  # output path

file_i = open(i_p, 'r')  # Reading the file
file_o = open(o_p, 'w')  # Writing into the file