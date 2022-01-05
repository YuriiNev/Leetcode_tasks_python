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

DB_dir = 'Databases/'
DB_input_name = 'leetcode_input.db'
DB_output_name = 'leetcode_output.db'


"""Filling input table."""


person_cnt = [['personId', 'INTEGER']
              ['lastName', 'TEXT'],
              ['firstName', 'TEXT']]  # Person_column_names_types

person_cn = []  # list of column names
for cname in person_cnt:
    person_cn.append(cname[0])
# end for cname in person_cnt:

person_table = [[1, "Wang", "Allen"],
                [2, "Alice", "Bob"],
                [3, "Bond", "James"],
                [4, "Shakespeare", "William"]]

address_cnt = [['addressId', 'INTEGER'],
               ['personId', 'INTEGER'],
               ['city', 'TEXT'],
               ['state', 'TEXT']]

address_cn = []  # list of column names
for cname in address_cnt:
    address_cn.append(cname[0])
# end for cname in person_cnt:

address_table = [[1, 2, 'Melbourne', 'Victoria'],
                 [2, 3, 'Sydney', 'NSW'],
                 [3, 7, 'New York City', 'New York'],
                 [4, 8, 'Leetcode', 'California'],
                 [5, 4, 'London', 'Britain']]

"""==============
  INPUT SECTION
=============="""

with sqlite3.connect(DB_dir+DB_input_name) as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS Person_175")

    SQL_st2 = sqf.SQL_CREATE_Table('Person_175')  # row_id = personId is already included
    cur.execute(SQL_st2)

    """ Initiating creation of the structure of Person_175"""
    for column_n_t in person_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column('Person_175',
                                    column_n_t[0],
                                    column_n_t[1])
        cur.execute(SQL_st)
    # end for column_n_t in person_cnt:

    """ The structure of the table Person_175 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(person_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          'Person_175',
          person_cn,
          person_table[i])
        a = sqf.SQL_CV_list(person_cn)
        b = sqf.SQL_CV_list(person_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(person_table)):
    """ Person_175 is filled."""

    cur.execute("DROP TABLE IF EXISTS Address_175")

    SQL_st1 = sqf.SQL_CREATE_Table('Address_175')  # row_id = adressId is already included
    cur.execute(SQL_st1)

    """ Initiating creation of the structure of Address_175."""
    for address_n_t in address_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column('Address_175',
                                    address_n_t[0],
                                    address_n_t[1])
        cur.execute(SQL_st)
    # end for address_n_t in address_cnt:

    """ The structure of the table Address_175 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(person_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          'Address_175',
          address_cn,
          address_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(person_table)):
    """ Address_175 is filled."""

"""===============
  OUTPUT SECTION
==============="""
