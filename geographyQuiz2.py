import random

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

for quizNum in range(35):
    quizFile=open(f'C:\\Users\\Administrator\\Desktop\\The long journey of programing\\quizes\\Mainexam\\capitals_quiz{quizNum+1}.txt','w')
    answersFile=open(f'C:\\Users\\Administrator\\Desktop\\The long journey of programing\\quizes\\answerforTheExam\\capitals_quiz{quizNum+1}.txt','w')
    
    quizFile.write('Name:_____\n\nClass:_____\n\nDate:____\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})\n\n')
    answersFile.write((' '*20)+'The answers for the quiz questions\n\n')
    
    states=list(capitals.keys())
    random.shuffle(states)
    
    #Get the right and the wrong answers
    
   
    #Create a loop that write the questions
    for questioNum in range(50):
        rightAnswer=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(rightAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answersOption=wrongAnswers+[rightAnswer]
        random.shuffle(answersOption)

        quizFile.write(f'What is the capital for {states[questionNum]}?\n\n')
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}.{answersOption[i]}\n\n")
        
        #put the right answer in a text file
        answersFile.write(f"{questionNum+1}.{'ABCD'[answersOption.index(rightAnswer)]}\n\n")
    quizFile.close()
    answersFile.close()