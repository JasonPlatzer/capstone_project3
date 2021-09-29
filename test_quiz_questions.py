import unittest
from unittest import TestCase
from unittest.mock import patch
from peewee import *

import quiz_questions

test_db = 'test_quiz.sqlite'
quiz_questions.db = test_db

from quiz_answer_table import QuizAnswer
from quiz_question_table import QuizQuestion


class TestQuiz(TestCase):
    

    def setUp(self):
        self.db = SqliteDatabase(test_db)
        self.db.drop_tables([QuizAnswer, QuizQuestion])
        self.db.create_tables([QuizAnswer, QuizQuestion])


    def test_add_question(self):
        quiz_questions.fill_table('question', 'correct_anser', 'wrong_answer1', 'wrong_answer2'
        'wrong_answer3','catagory', 20.0, 1, 'user_answer', True)
        self.db.drop_tables([QuizQuestion, QuizAnswer])
        self.db.create_tables([QuizQuestion, QuizAnswer])