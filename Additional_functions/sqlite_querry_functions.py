"""Additional functions for DB queries."""


def SQL_ADD_Column(table_name: str, column_name: str, cells_type: str):
    """Return SQL statement for adding columns.

    All variables supposed to be strings
    cell_type = ['TEXT', 'INTEGER', 'REAL', 'BLOB', 'NULL']
    """
    SQL_statement = "ALTER TABLE " + table_name
    SQL_statement += " ADD '" + column_name
    SQL_statement += "' '" + cells_type
    SQL_statement += "'"
    return SQL_statement


def SQL_UPDATE_Cell(table_name: str, column_name: str, row_id: int, cell_value):
    """Return SQL statement for updating a cell."""
    SQL_statement = "UPDATE " + table_name
    SQL_statement += " SET '" + column_name
    SQL_statement += "' = " + str(cell_value)
    SQL_statement += " WHERE row_id = " + str(row_id)
    return SQL_statement


def SQL_CREATE_Table(table_name: str):
    """Return SQL statement for creating a table.

    The Table has table_name and a technical column 'row_id'
    """
    SQL_statement = "CREATE TABLE IF NOT EXISTS " + table_name
    SQL_statement += """ ('row_id' INTEGER PRIMARY KEY AUTOINCREMENT)"""
    return SQL_statement


def SQL_INSERT_INTO(table_name: str, column_name: list, cell_value: list):
    """Return SQL statement for inserting a row into table.

    The Table has table_name; comn_name is a string of columns
    in format 'column1', 'column2', 'column3', ...; cell value is
    a string of values in format 'value1', 'value2', 'value3', ...;
    """
    SQL_statement = "INSERT INTO " + table_name
    SQL_statement += " (" + SQL_CV_list(column_name)
    SQL_statement += ")  VALUES (" + SQL_CV_list(cell_value)
    SQL_statement += ")"
    return SQL_statement


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
