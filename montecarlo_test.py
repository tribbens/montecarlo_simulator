import unittest
from montecarlo.montecarlo import Die
from montecarlo.montecarlo import Game
from montecarlo.montecarlo import Analyzer
import pandas as pd
import numpy as np

class MonteCarloTestSuite(unittest.TestCase):
    
    def test_1_init(self):
        die2 = Die(np.array([1, 2, 3, 4, 5, 6]))
        testing = type(die2) == Die
        message = "Dice setup not working correctly"
        
        self.assertTrue(testing, message)
        
    def test_2_weight_change(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        state1 = sum(die1.view_die()[0])
        die1.weight_change(1, 5)
        state2 = sum(die1.view_die()[0])

        status = state1 == state2
        message = "Changing weight not working correctly"
        
        self.assertFalse(status, message)
        
    def test_3_roll_die(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        status = type(die1.roll_die(10))
        type1 = list
        message = "roll_die method not working correctly"
        
        self.assertEqual(status, type1, message)
        
    def test_4_view_die(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        status = type(die1.view_die())
        type1 = pd.DataFrame
        message = "view_die not returning a pandas data frame"
        
        self.assertEqual(status, type1, message)
        
    def test_5_init(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game2 = Game([die1, die1, die1])
        
        testing = type(game2) == Game
        message = "Game setup not working correctly"
        
        self.assertTrue(testing, message)
        
    def test_6_play_game(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game1 = Game([die1, die1, die1])
        game1.play_game(100)
        
        testing = len(game1.recent_results()) == 100
        message = "play_game not working correctly"
        
        self.assertTrue(testing, message)
    
    def test_7_recent_results(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game1 = Game([die1, die1, die1])
        game1.play_game(100)
        
        testing = type(game1.recent_results()) == pd.DataFrame
        message = "recent_results not working correctly"
        
        self.assertTrue(testing, message)
        
    def test_8_init(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game1 = Game([die1, die1, die1])
        game1.play_game(100)
        analyzer2 = Analyzer(game1)
        
        testing = type(analyzer2) == Analyzer
        message = "Analyzer setup not working correctly"
        
        self.assertTrue(testing, message)
        
    def test_9_jackpot(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game1 = Game([die1, die1, die1])
        game1.play_game(100)
        analyzer1 = Analyzer(game1)
        
        testing = type(analyzer1.jackpot()) == int
        message = "jackpot method not working correctly"
        
        self.assertTrue(testing, message)
        
    def test_10_face_counts_per_roll(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game1 = Game([die1, die1, die1])
        game1.play_game(100)
        analyzer1 = Analyzer(game1)
        
        testing = type(analyzer1.face_counts_per_roll()) == pd.DataFrame
        message = "face_counts_per_roll not working correctly"
        
        self.assertTrue(testing, message)
        
    def test_11_combo_count(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game1 = Game([die1, die1, die1])
        game1.play_game(100)
        analyzer1 = Analyzer(game1)
        
        testing = type(analyzer1.combo_count()) == pd.DataFrame
        message = "combo_count not working correctly"
        
        self.assertTrue(testing, message)
        
    def test_12_permutation_count(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game1 = Game([die1, die1, die1])
        game1.play_game(100)
        analyzer1 = Analyzer(game1)
        
        testing = type(analyzer1.permutation_count()) == pd.DataFrame
        message = "permutation_count not working correctly"
        
        self.assertTrue(testing, message)
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
