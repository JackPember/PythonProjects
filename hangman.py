import random

logo = ''' 
 _    _                                         
| |  | |                                         
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| |__| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/  |                      
                   |____/    '''
print(logo)
attempts = 0
gallows = ['''            +---+
            |   |
                |
                |
                |
                |
                |
        ============''', '''                 
            +---+
            |   |
            O   |
                |
                |
                |
                |
        ============''', '''                    
            +---+
            |   |
            O   |
           /    |
                |
                |
                |
        ============''', '''                    
            +---+
            |   |
            O   |
           /|   |
                |
                |
                |
        ============''', '''                
            +---+
            |   |
            O   |
           /|\\  |
                |
                |
                |
        ============''', '''             
            +---+
            |   |
            O   |
           /|\\  |
           /    |
                |
                |
        ============''', '''                
            +---+
            |   |
            O   |
           /|\\  |
           / \\  |
                |
                |
        ============''', ]
wordList = ["scientist", "jolly", "cadaver", "horseshoe", "difficult", "poignant", "pungent", "jovial", "hummingbird",
            "colloquial", "pensive", "volcanic", "binomial", "polymorphism", "vector", "haberdashery", "neutron"]
display = ""
answer = random.choice(wordList)
validGuesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

length = len(gallows)
for character in answer:
    display += '_'

while attempts < 7:

    def display_answer(char, dis=display) -> list:  # change the display string to a list for showing the hint since
        # strings are immutable.
        index = 0
        dis = list(dis)
        for letter in answer:
            if answer[index] == char:
                dis[index] = char
            index += 1
        return dis


    print(" ".join(display))  # join with a space for better readability
    guess = str(input("Guess a letter: "))
    if guess not in validGuesses:
        print("Please enter a single lower-case letter!")
    elif guess not in answer:
        print(display)
        print(f"You guessed {guess}, that\'s not in the word. You lose a life.")
        if attempts <= length:
            print(gallows[attempts])
        attempts += 1
    elif guess in display:
        print("You already guessed that letter!")
    elif guess in answer:
        display = ''.join(display_answer(guess))  # join back into the full string to check if the word is equal to
        # the answer
    if attempts == 7:
        print(f"You ran out of lives, and did not guess the correct word, which was {answer}. "
              f"You lost, better luck next time!")
    if display == answer:
        print(f"You guessed {answer}, which was correct! You win!")
        break
