#Multiplication Quiz
#if you want to download the module that been used here type this in the cmd: pip install --user pyinputplus
import random,time
import operator
from threading import Timer

operators = {
    "+": operator.add,
    "-": operator.sub,
    "x": operator.mul,
    "/": operator.truediv,
    "pow": operator.pow
}


def Novice():
    global correctAnswers
    global numberOfQuestions
    for questionNumber in range(numberOfQuestions):

    #Pick two random numbers:
        num1=random.randint(0,9)
        num2=random.randint(0,9)

        prompt='#%s: %s x %s=' %(questionNumber,num1,num2)
        B=list(prompt)
        number1=int(B[4])
        number2=int(B[8])
        operator=B[6]
        func = operators.get(operator)
        answer=func(number1, number2)
        x=0
        while True:
            timeout = 8
            t = Timer(timeout, print, ['Sorry, times up, press enter to continue'])
            t.start()
            J=input(prompt)
            if J == str(answer):
                print('Correct')
                correctAnswers+=1
                time.sleep(1)
                t.cancel()
                break
            else:
                print ('Incorrect Answer')
                x+=1
                t.cancel()
                if x == 3:
                    print (f'The correct answer was {answer}')
                    break

def Moderate():
    global correctAnswers
    global numberOfQuestions
    print('Time increased to 16 seconds')
    for questionNumber in range(numberOfQuestions):

    #Pick two random numbers:
        num1=random.randint(0,9)
        num2=random.randint(0,9)
        num3=random.randint(0,9)

        prompt='#%s: %s x %s + %s=' %(questionNumber,num1,num2,num3)
        B=list(prompt)
        print(B)
        number1=int(B[4])
        number2=int(B[8])
        number3=int(B[12])
        operator1=B[6]
        operator2=B[10]
        func = operators.get(operator1)
        func2 = operators.get(operator2)
        answer=func(number1, number2)
        answer2=func2(answer,number3)
        x=0
        while True:
            timeout = 16
            t = Timer(timeout, print, ['Sorry, times up, press enter to continue'])
            t.start()
            J=input(prompt)
            if J == str(answer2):
                print('Correct')
                correctAnswers+=1
                time.sleep(1)
                t.cancel()
                break
            else:
                print ('Incorrect Answer')
                x+=1
                t.cancel()
                if x == 3:
                    print (f'The correct answer was {answer2}')
                    break
def Difficult():
    global correctAnswers
    global numberOfQuestions
    print('Time increased to 32 seconds\n Answer to the first decimal point e.g. 12.0')
    for questionNumber in range(numberOfQuestions):

    #Pick two random numbers:
        num1=random.randint(0,9)
        num2=random.randint(0,9)
        num3=random.randint(1,5)
        num4=random.randint(0,9)

        prompt='#%s: %s x %s / %s + %s=' %(questionNumber,num1,num2,num3,num4)
        B=list(prompt)
        number1=int(B[4])
        number2=int(B[8])
        number3=int(B[12])
        number4=int(B[16])
        operator1=B[6]
        operator2=B[10]
        operator3=B[14]
        func = operators.get(operator1)
        func2 = operators.get(operator2)
        func3 = operators.get(operator3)
        answer=func(number1, number2)
        answer2=func2(answer,number3)
        answer3=func3(answer2,number4)
        x=0
        while True:
            timeout = 32
            t = Timer(timeout, print, ['Sorry, times up, press enter to continue'])
            t.start()
            J=input(prompt)
            if J == str(answer3):
                print('Correct')
                correctAnswers+=1
                time.sleep(1)
                t.cancel()
                break
            else:
                print ('Incorrect Answer')
                x+=1
                t.cancel()
                if x == 3:
                    print (f'The correct answer was {answer3}')
                    break
while True:
    difficulty_level=input('What difficulty level do you want? Novice, Moderate, or Difficult: ')
    A=input('How many questions would you like: ')
    timeout = 8
    limits=3
    print(f'You have {timeout} seconds and {limits} attempts for each question\n')
    time.sleep(1)
    numberOfQuestions=int(A)
    correctAnswers=0
    if difficulty_level == 'Novice'.lower():
        Novice()
    if difficulty_level == 'Moderate'.lower():
        Moderate()
    if difficulty_level == 'Difficult'.lower():
        Difficult()


    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
    print()
    response=input('want to go for another round?\n')
    if response=='no':
        break
