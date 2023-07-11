import unittest
from hangman import HangmanGame

class HangmanGameTests(unittest.TestCase):
    def setUp(self):
        self.game = HangmanGame()

    def test_start_game(self):
        self.game.start_game()
        self.assertTrue(self.game.word in self.game.word_list)
        self.assertEqual(self.game.guessed_letters, [])
        self.assertEqual(self.game.attempts, 6)

    def test_guess_letter_correct(self):
        self.game.start_game()
        self.game.word = "apple"
        result = self.game.guess_letter("a")
        self.assertEqual(result, "a----")

    def test_guess_letter_incorrect(self):
        self.game.start_game()
        self.game.word = "apple"
        result = self.game.guess_letter("z")
        self.assertEqual(result, "incorret guess. You have 5 attempts left.")

    def test_guess_letter_already_guessed(self):
        self.game.start_game()
        self.game.word = "apple"
        self.guessed_letters = ["a", "p"]
        result = self.game.guess_letter("a")
        self.assertEqual(result, "You have already guessed that letter. Try again")

    def test_guess_letter_invalid_input(self):
        self.game.start_game()
        result = self.game.guess_letter("apple")
        self.assertEqual(result, "Please enter a single letter.")

    def test_game_win(self):
        self.game.start_game():
        self.game.word = "apple"
        self.game.guessed_letters = ["a", "p", "l", "e"]
        result = self.game.guess_letter("a")
        self.assertEqual(result, "Congratulation! You have guessed the word corretly")

    def test_game_loss(self):
        self.game.start_game()
        self.game.word = "apple"
        self.game.guessed_letters = ["b", "c", "d", "f", "g"]
        result = self.game.guess_letter("a")
        self.assertEqual(result, "Incorrect guess. You have 1 attempts left.")

        if __name__=="__main__":
            unittest.main()                

