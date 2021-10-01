from peewee import *
import unittest
from unittest import TestCase
from unittest.mock import patch
import quiz_questions

test_db = 'test_quiz.sqlite'
quiz_questions.db = test_db

from quiz_answer_table import QuizAnswer
from quiz_question_table import QuizQuestion


class TestQuiz(TestCase):
    

    def setUp(self):
        self.db = SqliteDatabase(test_db)
       # self.db.drop_tables([QuizAnswer, QuizQuestion])
        self.db.create_tables([QuizAnswer, QuizQuestion])


    def test_add_answer(self):
        
        #self.db.drop_tables([QuizQuestion, QuizAnswer])
    
        test_quiz = quiz_questions.fill_answer_table('2021-09-30 13:20:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, 'good guess', 'True', 'nhhy' )
        test_quiz.save()

    def test_add_without_info_will_error(self):
        #self.db.drop_tables([QuizQuestion, QuizAnswer])
        test_quiz = quiz_questions.fill_answer_table()
        with self.assertRaises(TypeError):
            test_quiz.save()

    def test_adding_only_strings_will_error(self):
        #self.db.drop_tables([QuizQuestion, QuizAnswer])
        test_quiz = quiz_questions.fill_answer_table('2021-09-30 13:20:47.723264','30.5','2021-09-30 13:21:47.723264', '258', 'good guess', 'True', 'nhhy' )
        with self.assertRaises(TypeError):
            test_quiz.save()
    
    def test_adding_numbers_where_a_stirng_should_be_will_error(self):
        with self.assertRaises(TypeError):
            test_quiz = quiz_questions.fill_answer_table('2021-09-30 13:20:47.723264','30.5','2021-09-30 13:21:47.723264', 258, 1, 2, 3 )
            test_quiz.save()
    
    def testdisplay_questions_will_only_work_with_a_correct_category(self):
        with self.assertRaises(TypeError):
            test_quiz = quiz_questions.display_questions(1,'nothing')
        
    def test_display_questions_will_only_work_with_a_correct_number_of_questions(self):
        with self.assertRaises(TypeError):
            test_quiz = quiz_questions.display_questions(21,'General Knowledge')

        
