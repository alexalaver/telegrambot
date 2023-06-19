import sqlite3

class Data:
    def __init__(self, name_data):
        self.connect = sqlite3.connect(name_data)
        self.cursor = self.connect.cursor()

    def add_question(self, question, answer):
        with self.connect:
            self.cursor.execute("INSERT INTO asks(question, answer) VALUES(?, ?);", (question, answer,))
            self.connect.commit()

    def del_question(self, question):
        with self.connect:
            self.cursor.execute("DELETE FROM asks WHERE question=?;", (question,))
            self.connect.commit()

    def select_question(self):
        with self.connect:
            return self.cursor.execute("SELECT question FROM asks;").fetchall()

    def select_question_answer(self, question):
        with self.connect:
            return self.cursor.execute("SELECT question, answer FROM asks WHERE question=?", (question,)).fetchall()