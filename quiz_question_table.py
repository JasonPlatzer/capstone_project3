
from peewee import *
import db_config

db = SqliteDatabase(db_config.database_name)


class QuizQuestion(Model):
    question_id = AutoField()
    question = CharField()
    correct_answer = CharField()
    wrong_answer1 = CharField()
    wrong_answer2 = CharField()
    wrong_answer3 = CharField()
    catagory = CharField()
    points_per_question = FloatField(constraints=[Check('points_per_question > 0')])
    # from https://stackoverflow.com/questions/25105188/python-peewee-how-to-create-a-foreign-key


    class Meta:
        database = db

    def __str__(self):
        return f'{self.question_id,}, {self.question}, {self.correct_answer}, {self.wrong_answer1}, {self.wrong_answer2}, {self.wrong_answer3}, {self.catagory}'
