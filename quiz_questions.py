import re
from peewee import *
from quiz_answer_table import QuizAnswer
from quiz_question_table import QuizQuestion
import requests
import json
import datetime
import random
import db_config
import uuid

db = SqliteDatabase(db_config.database_name)

# where I got the questions from, I put them in text so there are display issues-showing characters where letters should be


# results_general_knowledge = requests.get('https://opentdb.com/api.php?amount=50&category=9&type=multiple').text
# results_entertainment_television = requests.get('https://opentdb.com/api.php?amount=50&category=14&type=multiple').text
# results_science_computers = requests.get('https://opentdb.com/api.php?amount=50&category=18&type=multiple').text






#     #from https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0
    





def main():
    db.connect()
    db.create_tables([QuizAnswer, QuizQuestion])

    
    print('Welcome to the quiz.\nSelect the topic by number\n1. Science:Computers\n2. Entertainment:Television\n3. General Knowledge')
    ask_user()
    
    db.close()
    
    
    

def ask_user():
    category_name = ''
    return_category = ''
    
    ask_again = True
    while ask_again:
        topic = input('Select number: ')
        if topic.isnumeric(): 
            topic = int(topic)
            if 0 < topic  < 4:
                ask_again = False
            if topic == 1:
                category_name = 'Science: Computers'
                return_category = category_name
            if topic == 2:
                category_name = 'Entertainment: Television'
                return_category = category_name
            if topic == 3:
                category_name = 'General Knowledge'
                return_category = category_name
    
    get_num_of_questions(return_category)
        
def get_num_of_questions(return_category):
    print(return_category)
    num_of_questions = 0
    num_questions = True
    while num_questions:
        # checking to see if input is an number
        num_of_questions = input('Select number of questions to answer up to 20: ')
        if num_of_questions.isnumeric():
            # changing input to an ingteger
            num_of_questions = int(num_of_questions)
        
            if 0 < num_of_questions < 21:
                num_questions = False
    display_questions(num_of_questions,return_category)
        
def display_questions(num_of_questions, return_category):

    
    correct_answer = False
    # from https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/
    id_of_quiz_session = uuid.uuid4().hex
    
    
    # setting the points to 100 and giving all users the chance to get 100 points
    the_points_per_question = 100 / num_of_questions
    points_earned_total = 0 
    num_of_correct = 0
    # gets all the questions in that catagory, they are stored in groups in the database
    id_of_question = QuizQuestion.get(QuizQuestion.catagory == return_category)
    # gets the id of the first question
    id_of_question = id_of_question.question_id
    # I have to put this in another variable to work right
    x = id_of_question 
    start = datetime.datetime.now()
    print(start)    
    for  question in range(num_of_questions):
        # makes a list of all the question answer options to display
        answers_from_database = []
        # gets the first question
        quiz_questions = QuizQuestion.get(QuizQuestion.question_id == x)
        # sets the id of the answer to the id of the question
        id_of_question = quiz_questions.question_id
        start_of_question = datetime.datetime.now()
        # getting all the possible answers of the question and putting them in a list
        question_ask = quiz_questions.question
        print(question_ask)
        correct = quiz_questions.correct_answer
        answers_from_database.append(correct)
        wrong1 = quiz_questions.wrong_answer1
        answers_from_database.append(wrong1)
        wrong2 = quiz_questions.wrong_answer2
        answers_from_database.append(wrong2)
        wrong3 = quiz_questions.wrong_answer3
        answers_from_database.append(wrong3)
    
    
        random.shuffle(answers_from_database)
        # printing all the answer options
        for answer in answers_from_database:
            print(answer)
        user_guess = input('What is your guess ')
        # if user guesses correctly
        if user_guess == question_ask:
                correct_answer = True
                print('correct')
                num_of_correct += 1
                points_earned_total = points_earned_total + the_points_per_question
        print('incorrect')
        correct_answer = False
        end_of_question = datetime.datetime.now()
    # gets time of end of quiz    
    end_time = datetime.datetime.now()
    time_taken = end_time - start
    
        
    # from https://stackoverflow.com/questions/32211596/subtract-two-datetime-objects-python
        #print(str(time_taken.total_seconds()) + ' seconds')
    
    add_answer_table_row(start_of_question, points_earned_total, end_of_question, id_of_question, user_guess, correct_answer, question_ask, id_of_quiz_session)

        
    print(f'{time_taken} seconds to complete quiz, {num_of_questions} questions asked {num_of_correct} questions answered correct, 100 total points available, {points_earned_total} points earned, {points_earned_total} % on quiz')
    
def add_answer_table_row(start_of_question, points_earned_total, end_of_question, id_of_question, user_guess, correct_answer, question_ask, id_of_quiz_session):
    
        user_results = QuizAnswer(time_attempted=start_of_question,points_earned=points_earned_total, 
        time_of_finish=end_of_question, question_id=id_of_question,user_answer=user_guess,correct_or_not=correct_answer, question=question_ask, id_of_session=id_of_quiz_session)
        user_results.save()
    
        


    

        
                
if __name__ == '__main__':
    main()



#from https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0

    
