from peewee import *
from datetime import datetime
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
        # This test isn't checking what you think it is 
        # the check_is_same variable is a peewee ModelSelect object - it's not data from the database (yet)
        check_if_same = QuizAnswer.select(QuizAnswer.time_attempted == '2021-09-30 13:20:47.723264')

        # here's a funny thing though, these statements are the opposite of each other, and they both pass
        self.assertEqual(time_of_attempt, check_if_same)  # check same - passes
        self.assertNotEqual(time_of_attempt, check_if_same)  # check different - also passes! 

        # what's going on, and I had to read peewee source code to figure this out, is that 
        # peweee ModelSelect objects override the defaul comparing equals and comparing not equals 
        # python methods, with their own custom behavior which makes sense in peewee world but makes your tests 
        # behave weirldy when comparing a ModelSelect to a String. The ModelSelect is equal and not equal to unexpected things.

        # The important things here is that the assert statment is checking if two very different things 
        # are equal, so even though the test is passing, it's not checking what you want to check.
        # a test that does check your code, 

        # you need to get() or execute() to get the data, assuming you expect one result, .get is good 

        # the structure is Model.select().where(  ... your query here ... ).get() 

        # use a descriptive variable name - what data does this variable store? 
        answer_from_database = QuizAnswer.select().where(QuizAnswer.time_attempted == '2021-09-30 13:20:47.723264').get()
        
        datetime_of_attempt = datetime.fromisoformat(time_of_attempt)  # make a datetime from the string 
        self.assertEqual(datetime_of_attempt, answer_from_database.time_attempted)  # passes - compare the expected datatime to the one in the DB

        self.assertEqual(time_of_attempt, answer_from_database.time_attempted) # but this test fails - Peewee is storing time_attempted 
        # as a datetime object, which is not the same as a string



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
    
    
            
    
    


        
