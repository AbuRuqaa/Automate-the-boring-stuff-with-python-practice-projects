#!python 3
#randomQuizGerneator.py - Creates quizzes with questions and answers
#random order, along with the answer key.

import random
#The quiz data. Keys are stated and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
   'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 quiz files
for quizNum in range(35):
    #Create the quiz answer key files.
    quizFile=open(f'C:\\Users\\Administrator\\Desktop\\The long journey of programing\\quizes\\Mainexam\\capitalsquiz{quizNum+1}.txt','w')
    answerKeyFile=open(f'C:\\Users\\Administrator\\Desktop\\The long journey of programing\\quizes\\answerforTheExam\\capitalsquiz_answers{quizNum+1}.txt','w')
    
    #Write out the header for the quiz
    
    quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizFile.write((''*20)+f'State Capitalz Quiz(Form{quizNum+1})')
    quizFile.write('\n\n')
    
    #Shuffle the order of the states.
    states=list(capitals.keys())
    random.shuffle(states)
    
    #Loop through all 50 stated,making a question for each.
    for questionNum in range(50):
        
        #Get the right and wrong answers
        correctAnswer=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)
        
        #Write the question and the asnwer options to the quiz file
        quizFile.write(f'{questionNum+1}. What is the captial of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}.{answerOptions[i]}\n")
        quizFile.write('\n')
        
        #Write the answer key to a file.
        answerKeyFile.write(f"{questionNum+1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
        
        