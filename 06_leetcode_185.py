"""leetcode.com 185. Department Top Three Salaries.

Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key column for this table.
departmentId is a foreign key of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee.
It also contains the ID of their department.

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of a department and its name.

A company's executives are interested in seeing who earns the most money
in each of the company's departments. A high earner in a department is
an employee who has a salary in the top three unique salaries for that
department.
Write an SQL query to find the employees who are high earners in each of the departments.
Return the result table in any order.
The query result format is in the following example.


Example 1:

Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
Explanation:
In the IT department:
- Max earns the highest unique salary
- Both Randy and Joe earn the second-highest unique salary
- Will earns the third-highest unique salary

In the Sales department:
- Henry earns the highest salary
- Sam earns the second-highest salary
- There is no third-highest salary as there are only two employees.
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
t_names = ['Employee_185', 'Department_185', 'DepEmpSal_185']

"""================ Employee ================"""

# Employee_185 columns' names and types
#         personId, sirname, name
employee_cnt = [['Id', 'INTEGER'],
                ['Name', 'TEXT'],
                ['Salary', 'REAL'],
                ['departmentId', 'INTEGER']]

# a separate list of column names
employee_cn = []
for cname in employee_cnt:
    employee_cn.append(cname[0])
# end for cname in employee_cnt:

# Employee_185 table content
#         personId, sirname, name
employee_table = [[1, 'Joe', 87654.32, 1],
                  [2, 'Henry', 86654.32, 2],
                  [3, 'Sam', 85654.32, 3],
                  [4, 'Max', 84654.32, 4],
                  [5, 'Will', 83654.32, 4],
                  [6, 'Joe', 82654.32, 3],
                  [7, 'Hanna', 81654.32, 2],
                  [8, 'Samantha', 80654.32, 1],
                  [9, 'Lia', 88654.32, 2],
                  [10, 'Lia', 89654.32, 2],
                  [11, 'Peter', 97654.32, 3],
                  [12, 'Hanna', 94654.32, 4]]

"""================ Department ================"""

""" IT IS BETTER TO RESTRUCTURE THE INITIAL PART SO
THAT INITIAL TABLE NAMES COULD BE CYCLED! """

# Department_185 columns' names and types
#         personId, sirname, name
department_cnt = [['departmentId', 'INTEGER'],
                  ['departmentName', 'TEXT']]

# a separate list of column names
department_cn = []
for cname in department_cnt:
    department_cn.append(cname[0])
# end for cname in department_cnt:

# Department_185 table content
#         personId, sirname, name
department_table = [[1, 'IT'],
                    [3, 'Sales'],
                    [2, 'HR'],
                    [4, 'Testers']]

"""==============
  INPUT SECTION
=============="""

i_p = DB_dir+DB_input_name  # input path

with sqlite3.connect(i_p) as con:
    cur = con.cursor()
    """ creating Employee_185 table."""
    cur.execute("DROP TABLE IF EXISTS " + t_names[0])

    SQL_st = sqf.SQL_CREATE_Table(t_names[0])  # row_id column created automatically
    cur.execute(SQL_st)

    """ Initiating creation of the structure of t_names[0] = Employee_185"""
    for column_n_t in employee_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column(t_names[0],
                                    column_n_t[0],
                                    column_n_t[1])
        cur.execute(SQL_st)
    # end for column_n_t in employee_cnt:

    """ The structure of the table Employee_185 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(employee_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[0],
          employee_cn,
          employee_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(employee_table)):
    """ Employee_185 is filled."""

    """ creating Department_185 table."""
    cur.execute("DROP TABLE IF EXISTS " + t_names[1])

    SQL_st = sqf.SQL_CREATE_Table(t_names[1])  # row_id column created automatically
    cur.execute(SQL_st)

    """ Initiating creation of the structure of t_names[0] = Department_185"""
    for column_n_t in department_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column(t_names[1],
                                    column_n_t[0],
                                    column_n_t[1])
        cur.execute(SQL_st)
    # end for column_n_t in department_cnt:

    """ The structure of the table Department_185 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(department_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[1],
          department_cn,
          department_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(department_table)):
    """ Department_185 is filled."""

"""===============
  OUTPUT SECTION
==============="""

o_p = DB_dir + DB_output_name  # output path

inp = sqlite3.connect(i_p)  # must be closed in the end
outp = sqlite3.connect(o_p)   # must be closed in the end

""" creating table with the results =============="""

curo = outp.cursor()
curo.execute("DROP TABLE IF EXISTS " + t_names[2])

SQL_st = sqf.SQL_CREATE_Table(t_names[2])  # row_id column created automatically
curo.execute(SQL_st)

pc_cnt = [['departmentName', 'TEXT'],
          ['Name', 'TEXT'],
          ['Salary', 'REAL']]

""" Initiating creation of the structure of t_names[2] = DepEmpSal_185"""
for column_n_t in pc_cnt:  # [0] - column name; [1] - column type
    SQL_st = sqf.SQL_ADD_Column(t_names[2],
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

""" Creating the DepEmpSal_185 table =============="""
""" Reading needed data from the input tables"""
""" 1) Creating the list of departments with the structure depname[depId]"""
curi = inp.cursor()

SQL_st = "SELECT " + department_cn[0] + " FROM " + t_names[1]
dname = [None]*(len(curi.execute(SQL_st).fetchall())+1)
# dname[0] is always None due to starting numeration with 1

SQL_st = "SELECT * FROM " + t_names[1]
for row in curi.execute(SQL_st):
    dname[row[1]] = row[2]
# dname now contains the list of names of departments so that:
# dname[departmentIndex] = department name

DepEmpSal_val = [None]*len(pc_cnt)  # here len(pc_cnt) = 3
SQL_st = ("SELECT * FROM " + t_names[0] +
          " ORDER BY " + employee_cn[3] +
          ", " + employee_cn[2] + " DESC")


old_name = None
for row in curi.execute(SQL_st):
    if old_name != row[len(row)-1]:
        old_name = row[len(row)-1]
        k = 0
    if k < 3:
        DepEmpSal_val[0] = dname[row[len(row)-1]]  # departmentName
        # row[len(row)-1] is department index
        DepEmpSal_val[1] = row[len(row)-3]  # Name of the employee
        DepEmpSal_val[2] = row[len(row)-2]  # Salary
        # writing the row into the output table
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[2],
          pc_cn,
          DepEmpSal_val)
        curo.execute(SQL_st)
        k += 1

#  sqf.SQL_CV_list([pc_cn[0], pc_cn[2]])


outp.commit()  # commiting changes into output DB, do not commit into input DB
outp.close()  # outp = sqlite3.connect(o_p)
inp.close()  # inp = sqlite3.connect(i_p)
