import sqlite3
import junkinserts

class DBManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)

    def create_table(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                create table if not exists todo(
                    id integer primary key autoincrement,
                    project text,
                    task text,
                    description text)
                ''')

    def insert_test(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(junkinserts.insert_statement)

    def get_all(self):
        with self.conn:
            cursor = self.conn.cursor()
            statement = 'select id, project, task, description from todo'
            cursor.execute(statement)
            return cursor.fetchall()

    def get_by_id(self, id):
        with self.conn:
            cursor = self.conn.cursor()
            statement = 'select id, project, task, description from todo where id = ?'
            cursor.execute(statement, [id])
            return cursor.fetchall()

    def insert(self, project, task, description):
        with self.conn:
            cursor = self.conn.cursor()
            statement = 'insert into todo(project, task, description) values (?, ?, ?)'
            cursor.execute(statement, [project, task, description])

    def update(self, id, project, task, description):
        with self.conn:
            cursor = self.conn.cursor()
            statement = 'update todo set project = ?, task = ?, description = ? where id = ?'
            cursor.execute(statement, [project, task, description, id])

    def delete(self, id):
        with self.conn:
            cursor = self.conn.cursor()
            statement = 'delete from todo where id = ?'
            cursor.execute(statement, [id])

    def get_projects(self):
        with self.conn:
            cursor = self.conn.cursor()
            statement = 'select distinct project from todo'
            cursor.execute(statement)
            return [r[0] for r in cursor]