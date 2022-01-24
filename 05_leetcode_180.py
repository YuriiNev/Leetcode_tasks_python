"""leetcode.com Task 180. Consecutive Numbers.

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key for this table.


Write an SQL query to find all numbers
that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example.


Example 1:

Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively
for at least three times.
"""

import sqlite3
import sqlite_querry_functions as sqf

"""
FILES STRUCTURE:

Sqlite_querry_functions package is located in Additional_functions folder
(sqlite_querry_functions package);

Input and output databases are located in Databases folder;

Text filies inputs and outputs are located in Text_files folder

Databases names are the same as in the tasks but
with the number of task in the end, such as Person_175, Address_175 etc.
"""

"""=================
  DEFINITION SECTION
================="""

# please, check the existance of the following folder and files
DB_dir = 'Databases/'
DB_input_name = 'leetcode_input.db'
DB_output_name = 'leetcode_output.db'

"""Filling the input table."""

# t_names - the list of the table names
t_names = ['Nums_180', 'CNums_180']

"""================ nums ================"""

# Nums_180 columns' names and types
#         personId, sirname, name
nums_cnt = [['Id', 'INTEGER'],
            ['num', 'TEXT']]

# a separate list of column names
#         personId, sirname, name
nums_cn = []
for cname in nums_cnt:
    nums_cn.append(cname[0])
# end for cname in nums_cnt:

# Nums_180 table content
#         personId, sirname, name
nums_table = [[1, 'a'],
              [2, 'a'],
              [3, 'a'],
              [4, 3],
              [5, 3],
              [6, 3],
              [7, 2],
              [8, 4],
              [9, 1],
              [10, 1],
              [11, 1],
              [12, 1]]

cc = 'num'  # the main column for operations

"""==============
  INPUT SECTION
=============="""

i_p = DB_dir+DB_input_name  # input path

with sqlite3.connect(i_p) as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS " + t_names[0])

    SQL_st = sqf.SQL_CREATE_Table(t_names[0])  # row_id column created automatically
    cur.execute(SQL_st)

    """ Initiating creation of the structure of t_names[0] = Nums_180"""
    for column_n_t in nums_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column(t_names[0],
                                    column_n_t[0],
                                    column_n_t[1])
        cur.execute(SQL_st)
    # end for column_n_t in nums_cnt:

    """ The structure of the table Nums_180 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(nums_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[0],
          nums_cn,
          nums_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(nums_table)):
    """ Nums_180 is filled."""

"""===============
  OUTPUT SECTION
==============="""

o_p = DB_dir + DB_output_name  # output path

inp = sqlite3.connect(i_p)  # must be closed in the end
outp = sqlite3.connect(o_p)   # must be closed in the end

""" creating table with the results =============="""

curo = outp.cursor()
curo.execute("DROP TABLE IF EXISTS " + t_names[1])

SQL_st = sqf.SQL_CREATE_Table(t_names[1])  # row_id column created automatically
curo.execute(SQL_st)

pc_cnt = []  # was = nums_cnt  # creating the list of column names and types
# pc_cnt.remove(pc_cnt[0])  # now has new indexation
pc_cnt.append(['ConsecutiveNums', 'TEXT'])

""" Initiating creation of the structure of t_names[1] = CNums_180"""
for column_n_t in pc_cnt:  # [0] - column name; [1] - column type
    SQL_st = sqf.SQL_ADD_Column(t_names[1],
                                column_n_t[0],
                                column_n_t[1])
    curo.execute(SQL_st)
# end for column_n_t in person_cnt:

# a separate list of column names
pc_cn = []
for cname in pc_cnt:
    pc_cn.append(cname[0])
# end for cname in pc_cnt:
""" output table has been created ================"""

""" Consecutive Numbers in CNums_180 ================
the repetitive numbers have to be removed """

""" readinng the data"""
curi = inp.cursor()

SQL_st = "SELECT " + cc + " FROM " + t_names[0]

row_val = []  # the result is stored here

""" creating the list of symbols that appear 3 times consecutively """

""" 1) check the first and the second value, start with the 3d"""
cc_val = curi.execute(SQL_st).fetchall()
length_cc = len(cc_val)

if length_cc < 3:
    row_val = None
# end if
else:
    for i in range(2, length_cc):
        if cc_val[i-2] == cc_val[i-1] and cc_val[i-1] == cc_val[i]:
            row_val.append(cc_val[i][0])
        # end if
    # end for
    # removing the repetitive numbers using dict
    row_val = list(dict.fromkeys(row_val))
# end else

print(row_val)
for i in range(len(row_val)):
    SQL_st = sqf.SQL_INSERT_INTO(
      t_names[1],
      pc_cn,
      row_val[i])
    curo.execute(SQL_st)
# end for

outp.commit()  # commit changes into output DB, do not commit into input DB
outp.close()  # outp = sqlite3.connect(o_p)
inp.close()  # inp = sqlite3.connect(i_p)
