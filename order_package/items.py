from collections import defaultdict
# classes for all tools

class AllPurpose():
    '''
    All tools and armour can have Unbreaking and Mending.
    Swords and axes can have any one of the three damage multipliers, and they are both
    subclasses of AllPurpose so self.damages is an array of the damage multipliers.
    '''
    def __init__(self, desired=None) -> None:
        # incompatible: damages
        self.enchants = ['MEND', 'UNBR']
        self.damages = ['SHRP', 'SMTE', 'BANE']
        self.desired = desired
    
    def checker(self, desired) -> list:
        hmp = defaultdict(list)
        for e in desired:
            hmp[e in self.enchants].append(e)
        return hmp[False]
