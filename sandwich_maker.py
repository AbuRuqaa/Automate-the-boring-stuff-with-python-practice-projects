#!python3
#Sandwish maker
'''Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input'''
import pyinputplus as pyip

def sandwishMaker():
    prices={'wheat_cost': 1,
    'white_cost':5,
    'sourdough_cost':10,
    'chicken_cost':5,
    'turkey_cost':10,
    'ham_cost':20,
    'tofu_cost':25,
    'cheddar':2,
    'swiss':3,
    'mozzarella':5,
    'total_cost':0}
    
    wheat_cost= 1
    white_cost=5
    sourdough_cost=10
    chicken_cost=5
    turkey_cost=10
    ham_cost=20
    tofu_cost=25
    cheddar=2
    swiss=3
    mozzarella=5
    total_cost=0
    
        
             
    
    print('Welcome to sadwish Maker')
    print('if you want to see the list enter(yes)pls')
    list=pyip.inputYesNo()
    if list=='yes':
        for i,c in prices.items():
            print(i,':',c)
    print()
    print('We have 2 kind sadwiches') 
    breadChoices=pyip.inputMenu(['wheat','white','sourdough'],blank=True)
    proteinChoices=pyip.inputMenu(['chicken','turkey','ham','tofu'],blank=True)
        
    if breadChoices=='wheat':
        total_cost+=wheat_cost
    if breadChoices=='white':
        total_cost+=white_cost
    if breadChoices=='sourdough':
        total_cost+=sourdough_cost
    if breadChoices=='':
        total_cost+=0
    if proteinChoices=='chicken':
        total_cost+=chicken_cost
    if proteinChoices=='turkey':
        total_cost+=turkey_cost
    if proteinChoices=='ham':
        total_cost+=ham_cost
    if proteinChoices=='tofu':
        total_cost+=tofu_cost
    cheese=pyip.inputYesNo('Do you want cheese pls answer(yes/no) only:')
    if cheese=='yes':
        print('We have 3 kinds of cheese what do you want')
        cheeseMenu=pyip.inputMenu(['cheddar','Swiss','mozzarella'])
        if cheeseMenu=='cheddar':
            total_cost+=cheddar
        if cheeseMenu=='mozzarella':
            total_cost+=mozzarella
        if cheeseMenu=='Swiss':
            total_cost+=swiss
    
    print('Thank you for visiting us the total cost is '+str(total_cost))
    
                               
    
        
    
    
    
        
        
sandwishMaker()