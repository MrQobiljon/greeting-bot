import psycopg2

from config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database=DB_NAME,
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_group_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS groups(
            group_id BIGINT PRIMARY KEY
        )'''
        self.manager(sql, commit=True)

    def insert_group_id(self, group_id):
        sql = '''INSERT INTO groups(group_id)
        VALUES (%s)
        ON CONFLICT DO NOTHING'''
        self.manager(sql, (group_id,), commit=True)

    def select_groups_id(self):
        sql = '''SELECT group_id FROM groups'''
        return self.manager(sql, fetchall=True)