"""Based on the leetcode.com Task 192. Word Frequency.

Write a script to calculate the frequency of each word
in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.

Example: _______________________________________________________________

Assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:
the 4
is 3
sunny 2
day 1
________________________________________________________________________
"""

# import os

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
Text_input_name = '192_words.txt'
Text_output_name = '192_result.txt'

i_p = Text_dir + Text_input_name  # input path
o_p = Text_dir + Text_output_name  # output path

file_i = open(i_p, 'r')  # Reading file
file_o = open(o_p, 'w')  # Writing into file

exclude = [',', '.', '(', ')', "'", ';', '"', '!', '?', ':', "`"]
endings_1 = ['s ', 'ed ', 'ing ', '-', '\n']
endings_2 = ['s[', 'ed[', 'ing[']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# letters = []
# for i in range(65, 91):
#     letters.append(chr(i))
# for i in range(97, 123):
#     letters.append(chr(i))

words = []  # the list of words
numbers = []  # the list of numbers
links = []  # the list of links

file_text = file_i.read()

""" refining the initial string: 1) removeing punktuation marks """
for x in exclude:
    file_text = file_text.replace(x, "")

""" refining the initial string: 2) removeing endings, retaining the spaces"""
""" a little crude solution, for internal use only"""
fix_list = [' is', ' was', ' has', ' as']
for fl in fix_list:
    file_text = file_text.replace(fl, fl+'s')  # we are going
    # to remove added s in remobings ending section

for x in endings_1:
    file_text = file_text.replace(x, " ")

""" refining the initial string: 3) removeing endings with ["""
for x in endings_2:
    file_text = file_text.replace(x, "[")

""" refining the initial string: 3) removeing endings with numTH"""
for x in digits:
    file_text = file_text.replace(x+'th', x)
# print(file_text)

""" Creating the lists of objects (links, numbers and words)"""

w_flag = False
n_flag = False
l_flag = False
word = ''
number = ''
link = ''
for st in file_text:
    """ adding links to the list"""
    if st == '[':
        l_flag = True
    if st == ']':
        l_flag = False  # here, all three flags should be False
        link += st
        links.append(link)
        link = ''

    if l_flag is True:
        link += st

    """ adding numbers to the list"""
    if st in digits and l_flag is not True:
        n_flag = True
        number += st

    if n_flag is True and st == ' ':
        n_flag = False
        numbers.append(number)
        number = ''

    """ adding words to the list"""
    if l_flag is False and n_flag is False and st != ']' and st != ' ':
        w_flag = True
        word += st

    if w_flag is True and st == ' ':
        w_flag = False
        words.append(word)
        word = ''

if w_flag is True:
    w_flag = False
    words.append(word)
    word = ''

if n_flag is True:
    n_flag = False
    numbers.append(number)
    number = ''

""" The lists of objects (links, numbers and words) have been created"""

""" calculating the number of words"""

w_len = len(words)

words.sort()
dictionary = []  # the list with the results; even elements represent words,
# odd show quantity of the word
dictionary.append([words[0], 1])  # add 1st element
k = 0
for i in range(1, w_len):
    if words[i-1] == words[i]:
        dictionary[k][1] += 1
    else:
        dictionary.append([words[i], 1])  # add 1st element
        k += 1
    # end else
# end for

# sorting the results and writing it in the file
dictionary.sort(key=lambda x: x[1], reverse=True)

for i in range(len(dictionary)):
    file_o.write(str(dictionary[i][1]) + ' ' + dictionary[i][0] + '\n')

file_o.close()
file_i.close()
