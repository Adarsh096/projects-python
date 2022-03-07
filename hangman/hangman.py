# Working :
# The letters of the words have to be guessed.
# Player gets len(word)+2 chances to guess the word.

import random


class Hangman:
    def __init__(self,wordlist):
        self.wordlist = wordlist
    
    def pickWord(self):
        self.word = random.choice(self.wordlist)
        self.chances = len(self.word)+2
        self.guess_str = self.word[0]+"_"*(len(self.word)-2) + self.word[-1]
        
    def correctGuess(self,letter):
        idx = self.word.find(str(letter))
        return True if idx !=-1 else False

    def display(self,letter):
        # This modifies the guess string.
        # Find the position of letter and print it
        idx = self.word.find(letter)
        # Note : the left substring is captured by end index idx and not idx-1
        self.guess_str = self.guess_str[:idx]+ letter + self.guess_str[idx+1:]
        print(f"Good Guess : {self.guess_str}")

    def guess(self,letter):
        # handles the changes in chances left and update of output
        # returns gameover flag True if all chances are exhausted
        # or we have guessed the correct word.

        # reduce the chances left
        self.chances-=1

        if(self.correctGuess(letter)):
            # display the updated str
            self.display(letter)
        else:
            print("Aah! wrong guess")
        
        # if the game can not be continued then proactively end the game:
        if(self.chances < (len(self.word)-2) or self.guess_str.find('_') == -1):
            print(f"The correct word was : {self.word}")
            return True
        print(f"You have {self.chances} chance(s) left.")

    
if __name__ == "__main__":
    with open('words.txt') as f:
        wordlist = f.readlines()
    # remove the \n from readlines o/p list:
    wordlist = [line.rstrip() for line in wordlist]
    # print(wordlist[:10])

    # initialize the game:
    game_object = Hangman(wordlist)
    game_object.pickWord()
    print(f"Guess letters in this word : {game_object.guess_str}")
    while True:
        letter = input("What is your guess : ")
        if(letter != ''): # since all trailing new lines are stripped by input()
            game_over_flg = game_object.guess(letter)
            if game_over_flg:
                print("Game Over")
                break
        else:
            continue
