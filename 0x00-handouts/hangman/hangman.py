import random

def main():
    game_start = HangmanGame()
    game_start.start_game()


class HangmanGame:
    def __init__(self):
        self.word_list = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "rapefruit"]
        self.word = " "
        self.guessed_letters = []
        self.attempts = 6

    def start_game(self):
         self.word = random.choice(self.word_list)
         self.guessed_letters = []
         self.attempts = 6

    def guess_letter(self, letter):
        if len(letter) != 1:
            return "please enter a single letter."
        
        if letter in self.guess_letters:
            return "you have already guessed that letter. Try again."
        
        if letters not in self.word:
            self.attempts -= 1
            return "Incorret guess. You have {} attempt left.".format(self.attempts)
        else:
            self.guess_letters.append(letter)

        Word_progress = ""
        for char in self.word:
            if char in self.guessed_letters:
                word_progress += " "
            else:
                word_progress += "_ "

        if "_ " not in Word_progress:
            return "Congratulations! You guessed the word corretly."
        else:
            return Word_progress
        
def play_game():
    while True:
        game = HangmanGame()
        game.start_game()
        print("\nNew game! Guess the word:")
        print(game.guess_letter(""))
        while game.attempts > 0:
            letter = input("Enter a letter: ")
            result = game.guess_letter(letter)
            print(result)
            if "Congratulation" in result or "You ran out of attempts" in result:
                break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes"
            break

if __name__ == "__main__":
    main()       ss     
        

