import re

def valid_pass1():#You can enter the pass here
    strongPas=re.compile(r'[a-zA-Z]{8,}\d+')
    print('Please enter a password to check if its strong or not:')
    password=input()
    if strongPas.findall(password):
        print('Its a strong pass')  
    else:
        print('its not a strong password')
    print()

def valid_pass2(test):#the password is already written
    strongPas=re.compile(r'[a-zA-Z]{8,}\d+')
    if strongPas.findall(test):
        print(test+' is a strong pass')
        return True
    else:
        print(test+' isn`t a strong password')
        return False

valid_pass1()
print(valid_pass2('\nbannafishIsnotstrong'))
print(valid_pass2('\nNarutokunisNumber1'))
print(valid_pass2('Pretty good but not enough'))
       
