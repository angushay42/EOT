from collections import deque
# classes for all tools

class AllPurpose():
    '''
    All tools and armour can have Unbreaking and Mending.
    Swords and axes can have any one of the three damage multipliers, and they are both
    subclasses of AllPurpose so self.damages is an array of the damage multipliers.
    '''
    def __init__(self) -> None:
        # incompatible: damages
        self.enchants = ['MEND', 'UNBR']
        self.damages = ['SHRP', 'SMTE', 'BANE']
