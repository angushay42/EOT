import unittest

from order_package.items import AllPurpose



class TestAllPurpose(unittest.TestCase):
    def test_invalid(self):
        ap = AllPurpose()
        # Test if invalid enchants are returned correctly
        self.assertEqual(ap.checker(['IMPL','MEND','SHRP']),['IMPL','SHRP'])
        # Test if correct enchants are not returned 
        self.assertEqual(ap.checker(['MEND']),[])

    def test_mutual(self):
        ap = AllPurpose()
        # Instantiate an axe object without import.
        # Item can have only one from each list,
        ap.mutuals = [['FORT', 'SILK'], ['BANE','SHRP','SMTE']]

        # Test if input has more than one mutually exclusive enchantment 
        # from one pool.
        self.assertEqual(ap.mutual(['SILK','FORT']), True)
        self.assertEqual(ap.mutual(['SILK','SHRP']), False)
        # Test with two pools of mutually exclusive enchantments
        self.assertEqual(ap.mutual(['MEND','UNBR','FORT','SHRP']), False)
        self.assertEqual(ap.mutual(['MEND','UNBR','FORT','SILK','SHRP']), True)
        # No enchantments are vacuously true
        self.assertEqual(ap.mutual([]) , False)