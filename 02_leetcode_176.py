"""leetcode.com Task 176. Second Highest Salary.

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key column for this table.
Each row of this table contains information about the salary of an employee.

Write an SQL query to report the second highest salary from the Employee table.
If there is no second highest salary, the query should report null.

The query result format is in the following example.

Example 1:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
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
t_names = ['Salary_176', 'Second_HS_176']

"""================ Salary ================"""

# Salary_176 columns' names and types
#         personId, sirname, name
salary_cnt = [['Id', 'INTEGER'],
              ['salary', 'INTEGER']]

# a separate list of column names
#         personId, sirname, name
salary_cn = []
for cname in salary_cnt:
    salary_cn.append(cname[0])
# end for cname in salary_cnt:

# Salary_176 table content
#         personId, sirname, name
salary_table = [[1, 500],
                [2, 500],
                [3, 100],
                [4, 100]]

cc = 'salary'  # the main column for operations

"""==============
  INPUT SECTION
=============="""

i_p = DB_dir+DB_input_name  # input path

with sqlite3.connect(i_p) as con:
    cur = con.cursor()
    # t_names[0] = Salary_176
    cur.execute("DROP TABLE IF EXISTS " + t_names[0])

    SQL_st = sqf.SQL_CREATE_Table(t_names[0])  # row_id column created automatically
    cur.execute(SQL_st)

    """ Initiating creation of the structure of t_names[0] = Salary_176"""
    for column_n_t in salary_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column(t_names[0],
                                    column_n_t[0],
                                    column_n_t[1])
        cur.execute(SQL_st)
    # end for column_n_t in salary_cnt:

    """ The structure of the table Salary_176 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(salary_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[0],
          salary_cn,
          salary_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(salary_table)):
    """ Salary_176 is filled."""

"""===============
  OUTPUT SECTION
==============="""

o_p = DB_dir+DB_output_name  # output path

inp = sqlite3.connect(i_p)  # must be closed in the end
outp = sqlite3.connect(o_p)   # must be closed in the end

""" creating table with the results =============="""

curo = outp.cursor()
curo.execute("DROP TABLE IF EXISTS " + t_names[1])

SQL_st = sqf.SQL_CREATE_Table(t_names[1])  # row_id column created automatically
curo.execute(SQL_st)

pc_cnt = salary_cnt  # creating the list of column names and types
pc_cnt.remove(pc_cnt[0])  # now has new indexation

""" Initiating creation of the structure of t_names[1] = Second_HS_176"""
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
# end for cname in person_cnt:
""" output table has been created ================"""

""" defining the second highest salary in Salary_176 ==============
should be checked for several salaries of the same size and for absence
of the second salary.
"""

curi = inp.cursor()

# receing the values in the rows with personId in each table

SQL_st = "SELECT " + cc + " FROM " + t_names[0]
val_new = 0
val_old = 0

# after this cycle should be available 2 highest values from cc column
# here, problems with memory could occur in case of too long column
# more safe way is to use fetchone() untill it returns null
""" there are 3 values: val[0] - current value, val_old and val_new.
val_old should be < than val_new all the time (strong enequality),
except right before the change of val_new; when val_new maximized,
val_old should be maximsed as well"""
for i, val in enumerate(curi.execute(SQL_st).fetchall()):
    if val[0] > val_new:
        val_old = val_new
        val_new = val[0]
    # end if
    if i > 0 and val[0] > val_old and val[0] < val_new:
        val_old = val[0]
    # end if
# end for
print("pre-highest value = ", val_old, "highest value = ", val_new)


outp.commit()  # commiting changes into output DB, do not commit into input DB
outp.close()  # outp = sqlite3.connect(o_p)
inp.close()  # inp = sqlite3.connect(i_p)
