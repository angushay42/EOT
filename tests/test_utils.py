import unittest

from order_package.utils import level, level_cost, optimal


class test_utils(unittest.TestCase):
    def test_level(self):
        # Corectly calculates penalties of balanced trees.
        self.assertEqual(level(7)[0], 10)
        self.assertEqual(level(3)[0], 2)

        # Corectly calculates penalties of imbalanced trees.
        self.assertEqual(level(4)[0], 5)

        # Correctly calculates penalties with more enchantments than 
        # possible in-game.
        self.assertEqual(level(8)[0], 17)
        self.assertEqual(level(11)[0], 22)

        # Correctly calculates trees with no penalties.
        self.assertEqual(level(1)[1], [-1,0])

        # Correctly calculates trees for valid enchantment lists,
        # imbalanced and balanced.
        self.assertEqual(level(7)[1], [[[-1,0],[1,2]],[[3,4],[5,6]]])
        self.assertEqual(level(6)[1], [[[-1,0],[1,2]],[[3,4],5]])
        self.assertEqual(level(4)[1], [[[-1,0],[1,2]],3])

        # Correctly calculates trees for invalid enchantment lists, (not enough enchantments for one item).
        self.assertEqual(level(8)[1], [[[[-1, 0], [1, 2]], [[3, 4], [5, 6]]], 7])
        self.assertEqual(level(10)[1], [[[[-1, 0], [1, 2]], [[3, 4], [5, 6]]], [[7,8],9]])
        
        
    
    def test_level_cost(self):
        # Value representation of the wiki article's Boots diagram.
        desired = [12,12,6,4,4,3,2]
        
        # Correctly returns the total cost for valid sizes of input
        self.assertEqual(level_cost(desired), 58)
        self.assertEqual(level_cost(desired[:-1]), 52)
        self.assertEqual(level_cost([12,4,2]), 20)
        
        desired.append(4)
        invalid = sorted(desired, reverse=True)
        # Correctly returns the total cost for invalid sizes of input
        self.assertEqual(level_cost(invalid), 62)


        
        ''' ------- decremented tests for frequency map -------'''
        # # Returns correct map layout for trees with valid sizes (8 enchantments or less).
        # self.assertDictEqual(level_cost(len(desired)), {3:1,
        #                                                    2: 3,
        #                                                    1: 3})

        # # Returns correct map layout for trees with invalid sizes
        # # (not possible in game, but the formula continues).
        # self.assertDictEqual(level_cost(9),  {3: 1,
        #                                         2: 4,
        #                                         1: 4})

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