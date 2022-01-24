"""leetcode.com Task 178. Rank Scores.

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key for this table.
Each row of this table contains the score of a game.
Score is a floating point value with two decimal places.

Write an SQL query to rank the scores.
The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer
value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

The query result format is in the following example.

Example 1:

Input:
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output:
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
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
t_names = ['Rank_178', 'Place_178']

"""================ score ================"""

# Rank_178 columns' names and types
#         personId, sirname, name
score_cnt = [['Id', 'INTEGER'],
             ['score', 'REAL']]

# a separate list of column names
#         personId, sirname, name
score_cn = []
for cname in score_cnt:
    score_cn.append(cname[0])
# end for cname in score_cnt:

# Rank_178 table content
#         personId, sirname, name
score_table = [[1, 2.00],
               [2, 1.00],
               [3, 4.22],
               [4, 3.00],
               [5, 3.00],
               [6, 4.00],
               [7, 2.00],
               [8, 4.00],
               [9, 1.00],
               [10, 5.00],
               [11, 4.22],
               [12, 1.00]]

cc = 'score'  # the main column for operations

"""==============
  INPUT SECTION
=============="""

i_p = DB_dir+DB_input_name  # input path

with sqlite3.connect(i_p) as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS " + t_names[0])

    SQL_st = sqf.SQL_CREATE_Table(t_names[0])  # row_id column created automatically
    cur.execute(SQL_st)

    """ Initiating creation of the structure of t_names[0] = Rank_178"""
    for column_n_t in score_cnt:  # [0] - column name; [1] - column type
        SQL_st = sqf.SQL_ADD_Column(t_names[0],
                                    column_n_t[0],
                                    column_n_t[1])
        cur.execute(SQL_st)
    # end for column_n_t in score_cnt:

    """ The structure of the table Rank_178 is completed"""
    """ Initiating the filling of the table."""

    for i in range(len(score_table)):
        SQL_st = sqf.SQL_INSERT_INTO(
          t_names[0],
          score_cn,
          score_table[i])
        cur.execute(SQL_st)
    # end for i in range(len(score_table)):
    """ Rank_178 is filled."""

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

pc_cnt = score_cnt  # creating the list of column names and types
pc_cnt.remove(pc_cnt[0])  # now has new indexation
pc_cnt.append(['rank', 'INTEGER'])

""" Initiating creation of the structure of t_names[1] = Place_178"""
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

""" Rank Scores in Place_178 ================
the higher the score the higher the rank """

""" readinng the data"""
curi = inp.cursor()

SQL_st = "SELECT " + cc + " FROM " + t_names[0]
val_score = []

""" creating the list of values instead of the tuple """
for val in curi.execute(SQL_st):
    val_score.append(val[0])
# end for
val_score.sort(reverse=True)  # k*log(k) operations;

""" row_val[i] should be the list of two values: score, rank;
score is taken from val_score;
the task might be much more complicated
if Id should have been retained. """

# the first step
rank = 1  # defining the first rank
row_val = [val_score[0], rank]  # defining the list of rows

SQL_st = sqf.SQL_INSERT_INTO(
  t_names[1],
  pc_cn,
  row_val)
curo.execute(SQL_st)

# steps 2 to last
for i in range(1, len(val_score)):
    if val_score[i] < val_score[i-1]:  # val_score is sorted
        rank += 1
    # end if
    row_val = [val_score[i], rank]
    SQL_st = sqf.SQL_INSERT_INTO(
      t_names[1],
      pc_cn,
      row_val)
    curo.execute(SQL_st)
# end for i in range(1, len(val_score)):

outp.commit()  # commit changes into output DB, do not commit into input DB
outp.close()  # outp = sqlite3.connect(o_p)
inp.close()  # inp = sqlite3.connect(i_p)
