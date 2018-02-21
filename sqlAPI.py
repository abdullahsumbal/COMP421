import psycopg2


def getTables(cursor):

    cursor.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'cs421g29'""")

    # get all tables
    cursor.execute("""SELECT table_name FROM information_schema.tables
           WHERE table_schema = 'cs421g29'""")

    list_of_tables = []
    for table in cursor.fetchall():
        list_of_tables.append(table[0])
    return (list_of_tables)


def dropTable(cursor, table_name):

    cursor.execute("DROP TABLE "+table_name)

def clearTable(cursor, table_name, key):
    print("delete from "+table_name+" where "+key+"="+key+";")

    cursor.execute("delete from "+table_name+" where "+key+"="+key+";")


