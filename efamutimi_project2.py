'''
round_number(int) = tells the player what round the game is on
player_balance(int) = tells the player how much money they have and used for calculations
vowels(str) = used as a bank to not allow users to guess the same vowel over and over
vowel_cost(int) = used in calculations
comparer(str) = used to compare with the hidden characters when finding the index of the characters to replace
list(list) = separates the string into a list for easier string formatting/manipulation
hint(str) = the hint
bank(str) = the alphabet, so that users cant repeat cons. to farm money
variable(tuple) = allows for string manipulation
hidden_list(list) = allows for string manipulation to easily begin to display the underscores
hidden(str) = finalizes the display for the underscores for the player
prize(int/str) = takes the prize from the wheel
prize_multiplier(int) = used to count how many times the guessed cons. appears in the word, and used to multiply
index(int) = used to help replacing the hidden characters with the revealed characters
hoopty = used to define true or false to allow while loop to continue or end
chosen_vowel(str) = the vowel that the user chooses to buy
occurrence(int) = takes the amount of times that the vowel appears in the word
temp_vowels(str) = temp vowels when purchasing a cons. so that they can be guided to buy a vowel instead
guessed_consonant(str) = the consonant that the user guesses for the word
response(int) = used to guide player through branch of yes or no
yes_or_no(str) = used to guide the user through yes or no branches
choice(int) = used to guide the player through if else statements


break_apart():
pre- string must be a string.
post - creates comparer, used for comparisons in the code
round_start():
pre- for roundstart to be called, player_balance must be 250 or more
post- pulls the word that the user has to gues, along with creating hidden variable, or, tells user that there are no more words
end_game():
pre- user either has to go bankrupt, or income reaches below 0
post- ends the game/running code
consonant():
pre- guess_con has to be string, and in the bank. player_balance has to be above -1
post- player_balance is upgraded with the awards given in the function
buy_vowel():
pre- player must have above 250 to buy vowel, and also properly type in what vowel they want to purchase
post- vowel is purchased
player_choice():
pre- choice has to be an integer input
post- guides player to player_control() or other branches like buy_vowel() etc
win_screen():
pre- the word must be solved
post- the count of hidden characters is multiplied by the award of 950, player_bal is updated
player_control():
pre- the hidden word and hint is displayed
post- gives player the choice to play the game
'''

import helper

words = helper.PhrasesPrizeHelper()
words.add("School in New York", "SUNY Westchester Community College")
words.add("Clothing Brand", "Hollister")
words.add("During a moment of helplessness", "It is what it is")
words.add("Popular gaming laptop model", "Acer Predator Helios")
words.add("Film released in 1977", "Star Wars A New Hope")
words.add("80's song lyric", "Never gonna give you up never gonna let you down")
words.add("Popular espionage gaming franchise", "Metal Gear")
words.add("Source that professors hate", "Wikipedia")
words.add("Bested former heavyweight champion in 1996", "Evander Holyfield")
words.add("Writing instrument", "Ticonderoga Pencil")
words.add("Taste the rainbow", "Skittles")
words.add("Popular Shonen starting in 1984", "Dragon Ball")
words.add("Epiphany", "A change of heart")
words.add("Popular arcade", "Dave and Busters")
words.add("Fight", "Mortal Kombat")
words.add("Fight", "Street Fighter")
words.add("Division of government", "Federal Bureau of Investigation")
words.add("Predictions", "The weather app")
words.add("Identity", "Social security card")
words.add("Popular game show" , "Wheel of Fortune")
words.add("Major", "Computer science")
words.add("Major", "Computer information systems")
words.add("Event", "Birthday party")
words.add("Perspective", "the glass is half full")
words.add("Simple", "Piece of cake")
words.add("Bad mood", "Woke up on the wrong side of the bed")
words.add("Sweetener", "high fructose corn syrup")
words.add("Clicky Clacky", "Mechanical keyboard")
words.add("In Heat", "Talking in your sleep")
words.add("The Terminator", "arnold schwarzenegger")


round_number = 0
player_balance = 0000
vowels = 'aeiou'
vowel_cost = 250


def break_apart(string):
    global comparer
    list = string.split()
    for i, index in enumerate(list):
        list[i] = ' '.join(list[i])
    comparer = '    '.join(list)


def round_start():
    global vowels
    global string
    global hidden
    global round_number
    global hint
    global bank
    bank = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    variable = words.pull_random()
    if variable is None:
        print("There are no more words")
        end_game()
    else:
        round_number += 1
        print(f"Wheel Of Fortune: Round {round_number}\n")
        string = variable[1]
        hint = variable[0]
        list = string.split(' ')
        break_apart(string)
        hidden_list = []
        for word in list:
            hidden_word = '_ ' * len(word)
            hidden_list.append(hidden_word)
        hidden = '   '.join(hidden_list)

        print(hidden)
        print()


def end_game():
    if player_balance >= 0:
        print(f'You will be going home with ${player_balance}.')
        if round_number > 1:
            print(f'You played for {round_number} rounds.')
        else:
            print(f'You played for {round_number} round.')
        print("Thank you for playing!")
        exit()
    else:
        exit()


def consonant(guess_con, player_bal):
    global hidden
    global player_balance
    prize = words.prize()
    prize_multiplier = comparer.count(guess_con)
    if prize == 'Bankrupt':
        print("Spinning the wheel...")
        print("Oh no, you went bankrupt!")
        end_game()
    else:
        player_balance = player_bal + (prize * prize_multiplier)
        print(f'{guess_con} appears {prize_multiplier} times!')
        print("Spinning the wheel...")
        print(f'Your prize for this turn is {prize}!')
        print(f'You have been awarded {prize * prize_multiplier}. You new balance is {player_balance}.')
        print(f'Press Enter to Continue.')
        index = -1
        for times in range(prize_multiplier):
            index = comparer.find(guess_con, index + 1)
            hidden = hidden[0:index] + guess_con + hidden[index + 1:]
        input()
        print(hidden)


def buy_vowel():
    global player_balance
    global vowels
    global chosen_vowel
    global hidden
    hoopty = True
    while hoopty == True:
        chosen_vowel = input("Which vowel would you like to buy?\n").lower()
        if chosen_vowel in vowels:
            while hoopty == True:
                if len(chosen_vowel) == 1:
                    if chosen_vowel in comparer:
                        player_balance = player_balance - vowel_cost
                        print(f'You bought the vowel "{chosen_vowel}". Your new balance is {player_balance}')
                    else:
                        print(f'{chosen_vowel} does not appear in the word! Your balance is kept the same')
                        input()
                        print()
                        print(hidden)
                        player_control()
                    vowels = vowels.replace(chosen_vowel, '')  # removes purchased vowel from string

                    index = -1

                    occurrence = comparer.count(chosen_vowel)

                    if occurrence > 1:
                        print(f'The letter {chosen_vowel} appears {occurrence} times. Press Enter to continue')
                    else:
                        print(f'The letter {chosen_vowel} appears {occurrence} time. Press Enter to continue')
                    input()
                    for occurrences in range(occurrence):
                        index = comparer.find(chosen_vowel, index + 1)
                        hidden = hidden[0:index] + chosen_vowel + hidden[index + 1:]
                    print(hidden)
                    hoopty = False

                else:
                    print("You buy ONE vowel")
                    break
        else:
            print("It seems you already bought that vowel, or your input was not a vowel. Press Enter to Continue.")
            input()
            print(hidden)
            player_control()


def player_choice(choice):
    global player_balance
    global bank
    if choice == 1:
        temp_vowels = 'aeiou'
        guessed_consonant = input("Which consonant would you like to guess?\n").lower()
        if guessed_consonant in temp_vowels:
            print("Did you mean to buy a vowel?")
            print(f'{"Yes[1]":.<16} {"No[2]":.>16}')
            while True:
                response = int(input())
                if response == 1:
                    buy_vowel()
                    break
                if response == 2:
                    player_control()
                    break
                else:
                    print("Invalid Input- Please Try Again")
        elif guessed_consonant in comparer:
            if guessed_consonant in bank:
                bank = bank.replace(guessed_consonant, '')
                consonant(guessed_consonant, player_balance)
            else:
                print("You already guessed that consonant.\n")
                print(hidden)
                player_control()
        else:
            print("That consonant does not appear in this word.")
            print("Press Enter to Continue.\n")
            input()
            print(hidden)
            player_control()
    elif choice == 2:
        if player_balance >= vowel_cost:
            buy_vowel()
        else:
            print("You do not have enough to buy a vowel")
    elif choice == 3:
        player_word_guess = input("Enter the word/phrase: \n")
        if player_word_guess.lower() == string:
            win_screen(hidden, player_balance)
        else:
            print("Sorry, that is not quite right")
            print("$950 has been deducted from your balance. Press Enter to continue.\n")
            input()
            print(hidden)
            player_balance = player_balance - 950
            player_control()
    elif choice == 4:
        end_game()


def win_screen(hidden, player_bal):
    global player_balance
    print("Congrats, you solved the puzzle!\n")
    award_multiplier = hidden.count('_ ')
    player_balance = player_bal + (award_multiplier * 950)
    print(f'Your new balance is {player_balance}')
    print(f'Would you like to play again?\n')
    print(f'{"Yes[1]":.<16} {"No[2]":.>16}')
    while True:
        yes_or_no = input()
        if yes_or_no == "1":
            round_start()
            break
        elif yes_or_no == "2":
            end_game()
            break
        else:
            print("Invalid Input: Please Try Again")


def player_control():
    while comparer not in hidden:
        if player_balance >= 0:
            print(f'Hint: {hint}')
            print(f'{"Would you like to":~^30}')
            print(f'{"Guess a consonant?":.<30}{"[1]"}')
            print(f'{"Buy a vowel ($250)?":.<30}{"[2]"}')
            print(f'{"Solve the word/phrase?":.<30}{"[3]"}')
            print(f'{"Exit the game?":.<30}{"[4]"}\n')
            print(f'{"Player Balance:"}{player_balance:.>18}\n')
            while True:
                try:
                    choice = int(input())
                    if isinstance(choice, int):
                        player_choice(choice)
                        break
                except ValueError:
                    print("Invalid Input, Please Try Again")
        else:
            print("Sorry, you went bankrupt and lost the game! Better luck next time.")
            end_game()
    else:
        win_screen(hidden, player_balance)


while player_balance >= 0:
    round_start()
    player_control()
