from data.database_connection import *
import sqlite3


class Loginrepo:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [users(row["username"], row["password"]) for row in rows]

    def create_acc(self, varU, varP):
        cursor = self._connection.cursor()
        sqlite_insert_query = """INSERT INTO users
                            (username, password) 
                            VALUES 
                            (?, ?)"""
        record = (varU, varP)
        cursor.execute(sqlite_insert_query, record)
        self._connection.commit()
        cursor.close()
