from contextlib import closing

from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return []
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def all_category():
    sql = """
        select * from safia_category
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        data = dictfetchone(cursor)

    return data


def search_recipe(s):
    sql = f"""
    select * from safia_recipe
    where lower ("name") like lower('%{s}%')   
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)

    return data
