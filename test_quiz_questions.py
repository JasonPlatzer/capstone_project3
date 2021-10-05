from peewee import *
import unittest
from unittest import TestCase
from unittest.mock import patch
import db_config


db_config.database_name = 'test_quiz.sqlite'
import quiz_questions

from quiz_answer_table import QuizAnswer
from quiz_question_table import QuizQuestion


class TestQuiz(TestCase):
    

    def setUp(self):
        self.db = SqliteDatabase('test_quiz.sqlite')
        self.db.drop_tables([QuizAnswer, QuizQuestion])
        self.db.create_tables([QuizAnswer, QuizQuestion])
        
    def test_time_started_added_correctly(self):
        time_of_attempt = '2021-09-30 13:20:47.723264'
        quiz_questions.add_answer_table_row(time_of_attempt,30.5,'2021-09-30 13:21:47.723264', 258, 'good guess', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.time_attempted == '2021-09-30 13:20:47.723264')
        self.assertEqual(time_of_attempt, check_if_same)

    def test_points_earned_added_correctly(self):
        points = 30.5
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',points,'2021-09-30 13:21:47.723264', 258, 'good guess', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.points_earned == points)
        self.assertEqual(points, check_if_same)
    
    def test_id_of_question_added_correctly(self):
        id_of_question = 258
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', id_of_question, 'good guess', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.question_id == id_of_question)
        self.assertEqual(id_of_question, check_if_same)

    def test_time_ended_added_correctly(self):
        time_ended = '2021-09-30 13:21:47.723264'
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,time_ended, 258, 'good guess', 'True', 'nhhy', '410')
        check_if_same = QuizAnswer.select(QuizAnswer.time_of_finish == time_ended)
        self.assertEqual(time_ended, check_if_same)
   
    def test_answer_added_correctly(self):
        answer = 'good guess'
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, answer, 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.user_answer == answer)
        self.assertEqual(answer, check_if_same)
    
    def test_if_correct_added_correctly(self):
        correct = True
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, 'good guess', correct, 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.correct_or_not == correct)
        self.assertEqual(correct, check_if_same)

    def test_if_question_added_correctly(self):
        question_asked = 'is the sky blue'
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, 'good guess', True, question_asked, '401')
        check_if_same = QuizAnswer.select(QuizAnswer.question == question_asked)
        self.assertEqual(question_asked, check_if_same)

    
    def test_incorrect_time_fails(self):
        time_of_attempt = '2021-09-30 13:20:47.723264'
        quiz_questions.add_answer_table_row('2022-09-30 1:20:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, 'good guess', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.time_attempted == '2021-09-30 13:20:47.723264')
        self.assertNotEqual(time_of_attempt, check_if_same)

    def test_wrong_points_fails(self):
        points = 30.5
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',40.5,'2021-09-30 13:21:47.723264', 258, 'good guess', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.points_earned == points)
        self.assertNotEqual(points, check_if_same)
    
    def test_wrong_id_fails(self):
        id_of_question = 258
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', 1000, 'good guess', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.question_id == id_of_question)
        self.assertNotEqual(id_of_question, check_if_same)

    def test_wrong_end_time_fails(self):
        time_ended = '2021-09-30 13:21:47.723264'
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2022-09-30 13:21:47.723264', 258, 'good guess', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.time_of_finish == time_ended)
        self.assertNotEqual(time_ended, check_if_same)
   
    def test_wrong_answer_fails(self):
        answer = 'good guess'
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, 'wrong answer', 'True', 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.user_answer == answer)
        self.assertNotEqual(answer, check_if_same)
    
    def test_wrong_correct_or_not_fails(self):
        correct = True
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, 'good guess', False, 'nhhy', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.correct_or_not == correct)
        self.assertNotEqual(correct, check_if_same)

    def test_wrong_question_added_fails(self):
        question_asked = 'is the sky blue'
        quiz_questions.add_answer_table_row('2021-09-30 13:21:47.723264',30.5,'2021-09-30 13:21:47.723264', 258, 'good guess', True, 'wrong question', '401')
        check_if_same = QuizAnswer.select(QuizAnswer.question == question_asked)
        self.assertNotEqual(question_asked, check_if_same)



    
            
    
    


        
