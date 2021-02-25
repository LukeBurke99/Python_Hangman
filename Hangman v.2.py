## Hangman version 1
import random
print('This is a Hangman game!')
print('')
#   Making the object that the man will be hanged from and drawing his body 
def draw(a):

    print(' \n' * 5)
    #    draw the hanging man
    print(' ________')
    print(' |      |')
    print(' |     ',hanging[0])
    print(' |   ',hanging[1],hanging[2],hanging[3])
    print(' |    ',hanging[4],hanging[5])
    print(' |     ')
    print('-------\n')
 
         
#                                                                                 VARIABLES                                                                    #


b = 0   #   This distinguishes what body part will be added next
newFilm = ''   #   If the user wants to input a new film then it will be stored in this
tries = 6    #    The amount of lives the user has left
hanged , hanging = ['O','-','|','-','/','\\'],['','','','','',''] # This depends on the number of lives left
guess = []   #   the variable that will store the film we are guessing
guessed = []   #   the list that will store all the letters we have used
#   List of films    
films = ['shrek','harry potter','the incredibles','the avengers','finding nemo','batman','terminator','the godfather','the good the bad and the ugly',
         'the lord of the rings','forest gump','the matrix','psycho','alien','the shinning','toy story','the thing','fantastic four','indiana jones',
         'x men','scarface','up','et','the wolf of wall street','v for vendetta','how to train your dragon','12 years a slave','transformers',
         'planet of the apes','life of brian','the wizard of oz','million dollar baby','rocky','monsters inc','the hulk','gravity','black swan',
         'jurassic park','beauty and the beast','slumdog millionaire','judgement day','the lion king','the shawshank redemption','pretty woman','scream',
         'scary movie','ride along','robocop','after earth','enders game','21 jump street','world war z','die hard','grown ups','white house down','frozen']

#                                                                                 VARIABLES                                                                    #



#   the program picks a film at random (out of out film list)
film = random.randint(0, len(films)-1)
film = films[film]
film = list(film)                      #   This seperates the letters in the film chosen, meaning we can target every single letter.
 

# the program indicates how many letters are in the film
for i in range(len(film)):
    if film[i].isalpha():  #  if it is a letter in the film then ' _ ' will be shown
        guess += '_'
    else:
        guess += ' '  #  if it is a space in the film then a space between words will be shown


# Main while loop for the game

#    Checking to see if the user has lives left
while tries != 0 :
    draw(hanging) 
    
    print(' '.join(guess))   #   prints out the indication for the film
    
    guesses = ', '.join(guessed)  
    print('Letters guessed: ' , guesses )   #   prints the letters that have been guessed in this game
    
    print(tries,'lives left')   #  prints how many lives the user has left
    
    letter = input('Enter a letter: ')   #  allows the user to guess a letter
    letter = letter.lower()
    
#    checking if there is more than one letter
#    checking the input is a letter and not a number
#    checking the letter has not already been inputted.    
    while len(letter) > 1 or letter.isalpha() == False or letter in guessed:   #    continuesly ask until requirements are met
        letter = input("Enter 'one letter' that has not been used: ")
    guessed.append(letter)   #    add to guessed letters

#   checking if the letter is in the film
    for i in range(len(film)):
        if film[i] == letter:
            guess[i] = letter   #    if the letter is in the film then show it in the indicated title

#    if the letter is not in the film then minus a life
    if  letter not in film:
        tries -= 1
        hanging[b] = hanged[b]   #   add a body part to the nuse
        b += 1
        
#    checking if the user has guessed the film yet
    if guess == film:
        print('Well done!')
        break   #   end while loop if this is true
    
draw(hanging)

#  if the game is over then print the film and score them out of 6 (depending on how many lives they have left)
film = ''.join(film)
print('The answer was,', film +'. Your score is',tries,'/ 6')

#   Allow the user to enter a new film if they want to
while newFilm != 'y' and newFilm != 'n':
    print('Would you like to enter your own film? \'y\' or \'n\'')
    newFilm = input()
if newFilm == 'y':
    newFilm = input('Film:  ')
else:
    print('Thank you for playing')
