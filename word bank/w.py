import random
bank=['ps','sp']
word=random.choice(bank)

guessedword=['_']*len(word)


a=10

while a>0:
    print('\nCurrent word  '+' '.join(guessedword))
    guess=input('Enter guess ').lower()
    for i in range (len(word)):
     if word[i]==guess:
       guessedword[i]=guess
       print('Great guess ')
     else:
         a-=1
         print ('\nwrong guess attempts left '+str(a))
     if '_' not in guessedword:
         print('\ncongrats you guessed the word correctly ' +word)
         break
     if a==1:
          print('\nyou have no more guesses left \n The word was '+word)      
    
