from peewee import *
from quiz_question_table import QuizQuestion

db = SqliteDatabase('quiz.sqlite')


class QuizAnswer(Model):
    
    
    
    time_attempted = DateTimeField()
    points_earned = FloatField(constraints=[Check('points_earned > 0')])
    time_of_finish = DateTimeField()
    question_id = ForeignKeyField(QuizQuestion, to_field='question_id')
    user_answer = CharField()
    correct_or_not = CharField()
    question = CharField()
    

    class Meta:
        database = db

    def __str__(self):
        return f'  {self.time_attempted}, {self.points_earned}, {self.time_of_finish}, {self.id}, {self.user_answer},{self.correct_or_not}, {self.question}'




