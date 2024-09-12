import unittest

from order_package.utils import level, level_cost, optimal


class test_utils(unittest.TestCase):
    def test_level(self):
        # Corectly calculates penalties of imbalanced trees.
        # Correctly calculates trees with no penalties.
        # Correctly calculates trees with more enchantments than 
        # possible in-game.
        pass
    
    def test_level_cost(self):
        # Value representation of the wiki article's Boots diagram.
        desired = [12,12,6,4,4,3,2]
        
        # Returns correct map layout for trees with valid sizes (8 enchantments or less).
        self.assertDictEqual(level_cost(len(desired)), {3:1,
                                                           2: 3,
                                                           1: 3})

        # Returns correct map layout for trees with invalid sizes
        # (not possible in game, but the formula continues).
        self.assertDictEqual(level_cost(9),  {3: 1,
                                                2: 4,
                                                1: 4})

        

    def test_optimal(self):
        # Value representation of the wiki article's Boots diagram.
        desired = [12,12,6,4,4,3,2]

        # Returns the correct total cost
        self.assertEqual(optimal(desired)[0], 66)

        # Returns the correct the order of enchantments for even size
        self.assertEqual(optimal(desired)[1], [[-1,0],[6,1],[5,2],[4,3]])
        
        # Returns the correct the order of enchantments for odd size
        self.assertEqual(optimal(desired[:-1])[1], [[-1,0],[5,1],[4,2],3])
        self.assertEqual(optimal(desired[:-3])[1], [[-1,0],[3,1],2])

        # Handles "Too Expensive"
        too_expensive = [12,12,6,4,4,3,2,6,6,7,6]
        self.assertEqual(optimal(too_expensive), (0,[]))

        # Handles no pairs
        no_pairs = [12]
        self.assertEqual(optimal(no_pairs), (no_pairs[0], [[-1,0]]))

        # Handles no enchantments
        self.assertEqual(optimal([]),(0,[]))