import unittest
from unittest.mock import patch
import pokemon_1

class PokemonGameTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['WrongGuess1', 'WrongGuess2', 'CorrectGuess'])
    def test_pokemon_game(self, mock_input):
        # call the game function
        pokemon_game()

        # assertions
        captured = self.capsys.readouterr()
        self.assertIn("That's not the right Pokémon. Try again!", captured.out)
        self.assertIn("Congratulations! You guessed the Pokémon correctly!", captured.out)

if __name__ == '__main__':
    unittest.main()