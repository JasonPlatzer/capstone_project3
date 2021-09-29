import re
from peewee import *
from quiz_answer_table import QuizAnswer
from quiz_question_table import QuizQuestion
import requests
import json
import datetime
import random

db = SqliteDatabase('quiz.sqlite')
# results_general_knowledge = requests.get('https://opentdb.com/api.php?amount=50&category=9&type=multiple').text
# results_entertainment_film = requests.get('https://opentdb.com/api.php?amount=50&category=9&type=multiple').text
# results_entertainment_television = requests.get('https://opentdb.com/api.php?amount=50&category=14&type=multiple').text
# results_science_computers = requests.get('https://opentdb.com/api.php?amount=50&category=18&type=multiple').text



# general_knowledge = json.loads(results_general_knowledge)
# entertainment_film = json.loads(results_entertainment_film)
# entertainment_television = json.loads(results_entertainment_television)
# science_computers = json.loads(results_science_computers)





#     #from https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0
    





def main():
    db.connect()
    db.create_tables([QuizAnswer, QuizQuestion])

    
    print('Welcome to the quiz.\nSelect the topic by number\n1. Science:Computers\n2. Entertainment:Television\n3. General Knowledge')
    ask_user()
    db.close()
    
    
    

def ask_user():
    category_name = ''
    num_of_questions = 0
    ask_again = True
    while ask_again:
        topic = input('Select number: ')
        if topic.isnumeric(): 
            topic = int(topic)
            if 0 < topic  < 4:
                ask_again = False

                num_questions = True
                while num_questions:
                    num_of_questions = input('Select number of questions to answer up to 20: ')
                    if num_of_questions.isnumeric():
                        num_of_questions = int(num_of_questions)
                        return_num = num_of_questions
                        if 0 < num_of_questions < 21:
                            num_questions = False
        

                if topic == 1:
                    category_name = 'Science: Computers'
                    return_category = category_name
                if topic == 2:
                    category_name = 'Entertainment: Television'
                    return_category = category_name
                if topic == 3:
                    category_name = 'General Knowledge'
                    return_category = category_name
            

    display_questions(num_of_questions, category_name)
        
def display_questions(num_of_questions, category_name):
    correct_answer = False
    id_of_session = random.randint(1, 1000000)

    the_points_per_question = 100 / num_of_questions
    points_earned_total = 0 
    x = 0
    id_of_question = QuizQuestion.get(QuizQuestion.catagory == category_name)
    id_of_question = id_of_question.id
    x = id_of_question 
    start = datetime.datetime.now()
    print(start)    
    for  question in range(num_of_questions):
        
        answers_from_database = []
        quiz_questions = QuizQuestion.get(QuizQuestion.id == x)
        id_of_question = quiz_questions.id
        start_of_question = datetime.datetime.now()
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
        for answer in answers_from_database:
            print(answer)
        user_guess = input('What is your guess ')
        if user_guess == question_ask:
                correct_answer = True
                print('correct')
                points_earned_total = points_earned_total + the_points_per_question
        print('incorrect')
        correct_answer = False
        end_of_question = datetime.datetime.now()
       
        user_results = QuizAnswer(time_attempted=start_of_question,points_earned=points_earned_total,
        time_of_finish=end_of_question, id=id_of_question,user_answer=user_guess,correct_or_not=correct_answer, question=question_ask)
        user_results.save()
    end_time = datetime.datetime.now()
    time_taken = end_time - start
    # from https://stackoverflow.com/questions/32211596/subtract-two-datetime-objects-python
    print(str(time_taken.total_seconds()) + ' seconds')
        
   
            
        
                
if __name__ == '__main__':
    main()



#from https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0

    
