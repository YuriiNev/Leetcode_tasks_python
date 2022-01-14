"""leetcode.com Task 175. Combine Two Tables.

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key column for this table.
This table contains information about the ID of some persons and their first and last names.

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key column for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.


Write an SQL query to report the first name, last name,
city, and state of each person in the Person table. If the
address of a personId is not present in the Address table,
report null instead.

Return the result table in any order.

The query result format is in the following example.

Input:
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output:
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation:
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.
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
t_names = ['Person_175', 'Address_175', 'Person_Address_175']

"""================ Person ================"""

# Person_175 columns' names and types
person_cnt = [['personId', 'INTEGER'],
              ['lastName', 'TEXT'],
              ['firstName', 'TEXT']]

# a separate list of column names
person_cn = []
for cname in person_cnt:
    person_cn.append(cname[0])
# end for cname in person_cnt:

# Person_175 table content
#         personId, sirname, name
person_table = [[1, "Wang", "Allen"],
                [2, "Alice", "Bob"],
                [3, "Bond", "James"],
                [4, "Shakespeare", "William"]]

"""================ Address ================"""

# Address_175 columns' names and types
address_cnt = [['addressId', 'INTEGER'],
               ['personId', 'INTEGER'],
               ['city', 'TEXT'],
               ['state', 'TEXT']]

# a separate list of column names
address_cn = []
for cname in address_cnt:
    address_cn.append(cname[0])
# end for cname in person_cnt:

# Address_175 table content
#    addressId, personId, city,      state
address_table = [[1, 2, 'Melbourne', 'Victoria'],
                 [2, 3, 'Sydney', 'NSW'],
                 [3, 7, 'New York City', 'New York'],
                 [4, 8, 'Leetcode', 'California'],
                 [5, 4, 'London', 'Britain']]

cc = 'personId'  # common column by which tables are merging

"""==============
  INPUT SECTION
=============="""

i_p = DB_dir+DB_input_name  # input path

with sqlite3.connect(i_p) as con:
    cur = con.cursor()
    # t_names[0] = Person_175
    cur.execute("DROP TABLE IF EXISTS " + t_names[0])

    SQL_st = sqf.SQL_CREATE_Table(t_names[0])  # row_id column created automatically
    cur.execute(SQL_st)

    """ Initiating creation of the structure of t_names[0] = Person_175"""
    for column_n_t in person_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column(t_names[0],
                                    column_n_t[0],
                                    column_n_t[1])
        cur.execute(SQL_st)
    # end for column_n_t in person_cnt:

    """ The structure of the table Person_175 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(person_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[0],
          person_cn,
          person_table[i])
        a = sqf.SQL_CV_list(person_cn)
        b = sqf.SQL_CV_list(person_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(person_table)):
    """ Person_175 is filled."""

    # t_names[1] = Address_175
    cur.execute("DROP TABLE IF EXISTS " + t_names[1])

    SQL_st = sqf.SQL_CREATE_Table(t_names[1])  # row_id column created automatically
    cur.execute(SQL_st)

    """ Initiating creation of the structure of Address_175."""
    for address_n_t in address_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column(t_names[1],
                                    address_n_t[0],
                                    address_n_t[1])
        cur.execute(SQL_st)
    # end for address_n_t in address_cnt:

    """ The structure of the table Address_175 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(address_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[1],
          address_cn,
          address_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(person_table)):
    """ Address_175 is filled."""

"""===============
  OUTPUT SECTION
==============="""

o_p = DB_dir+DB_output_name  # output path

inp = sqlite3.connect(i_p)  # must be closed in the end
outp = sqlite3.connect(o_p)   # must be closed in the end

""" creating table with the results =============="""

curo = outp.cursor()
curo.execute("DROP TABLE IF EXISTS " + t_names[2])

SQL_st = sqf.SQL_CREATE_Table(t_names[2])  # row_id column created automatically
curo.execute(SQL_st)

pc_cnt = person_cnt  # creating the list of column names and types
for val in address_cnt:
    if val not in pc_cnt:
        pc_cnt.append(val)
    # end if val not in pc_cnt
# end for val in address_cnt
pc_cnt.remove(pc_cnt[0])  # has new indexation after removing an element
pc_cnt.remove(pc_cnt[2])

""" Initiating creation of the structure of t_names[2] = Person_Address_175"""
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
# end for cname in person_cnt:
""" output table has been created ================"""

""" merging columns with personId =============="""

curi = inp.cursor()

# receing the values in the rows with personId in each table
t0_cc = []
SQL_st = "SELECT " + cc + " FROM " + t_names[0]
for val in curi.execute(SQL_st).fetchall():
    t0_cc.append(val)
# end for

t1_cc = []
SQL_st = "SELECT " + cc + " FROM " + t_names[1]
for val in curi.execute(SQL_st).fetchall():
    t1_cc.append(val)
# end for

"""
1) check personId in the 1 table,
2) take the values of the corresponding row from the 1 table
3) check if the second table has the same personId value
3.5) delete the value from the list for preventing a double usage
4) take the values of the corresponding row from the 2 table
5) add values from 4) to the list with values from 2)
6) write the list into the table 3
"""
for val in t0_cc:
    row_val = []
    SQL_st = "SELECT * FROM " + t_names[0] + " WHERE " + cc + " = " + str(val[0])
    cc_t0 = curi.execute(SQL_st).fetchone()
    # adding into the resulting row all values except for the first 2
    for i in range(len(cc_t0)-2):
        row_val.append(cc_t0[i+2])
    # end for

    if val in t1_cc:
        SQL_st = "SELECT * FROM " + t_names[1] + " WHERE " + cc + " = " + str(val[0])
        cc_t1 = curi.execute(SQL_st).fetchone()
        # adding into the resulting row all values except for the first 3
        for j in range(len(cc_t1)-3):
            row_val.append(cc_t1[j+3])
        # end for
        t1_cc.remove(val)
    # end if val in t1_cc:
    else:
        for i in range(len(address_cn)-2):  # -2 (not -3) due to automatical column
            row_val.append('Null')
        # end for
    # end else
    # writing the row into the output table
    SQL_st = sqf.SQL_INSERT_INTO(
      t_names[2],
      pc_cn,
      row_val)
    curo.execute(SQL_st)
    # end for i in range(len(person_table)):

"""
1) check the remaining list of personalId -> t1_cc,
2) for each value in the list take the corresponding row
3) create the row for the new table with absent columns filled with None
4) write the row into the table
"""

for val in t1_cc:  # only elemens different from t0_cc remains
    row_val = []
    for i in range(len(person_cn)-1):  # -1 (not -2) due to automatical column
        row_val.append('Null')
    # end for
    SQL_st = "SELECT * FROM " + t_names[1] + " WHERE " + cc + " = " + str(val[0])
    cc_t1 = curi.execute(SQL_st).fetchone()
    # adding into the resulting row all values except for the first 3
    for j in range(len(cc_t1)-3):
        row_val.append(cc_t1[j+3])
    # end for
    # writing the row into the output table
    SQL_st = sqf.SQL_INSERT_INTO(
      t_names[2],
      pc_cn,
      row_val)
    curo.execute(SQL_st)


""" columns with personId have been merged into cc_me list =============="""
outp.commit()  # commiting changes into output DB, do not commit into input DB
outp.close()  # outp = sqlite3.connect(o_p)
inp.close()  # inp = sqlite3.connect(i_p)
