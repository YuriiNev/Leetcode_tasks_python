def SQL_CV_list(column_names: list):
    """Return SQL statement for several column names or values.

    Example: [name1, name2, name3] returned as a string:
    "name1', 'name2', 'name3'"
    the same is true for values too.
    """
    SQL_statement = ""
    for el in enumerate(column_names):
        SQL_statement += "'"
        if el[0] < len(column_names) - 1:
            SQL_statement += str(el[1]) + "',"
        else:
            SQL_statement += str(el[1]) + "'"
    return SQL_statement

person_cnt = [['lastName', 'TEXT'],
              ['firstName', 'TEXT']]  # Person_column_names_types

person_cn = []  # list of column names
for cname in person_cnt:
    person_cn.append(cname[0])
# end for cname in person_cnt:

a = SQL_CV_list(person_cn)
b=5