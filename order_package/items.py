from collections import defaultdict

class AllPurpose():
    '''
    All tools and armour can have Unbreaking and Mending.
    Swords and axes can have any one of the three damage multipliers, and they are both
    subclasses of AllPurpose so self.damages is an array of the damage multipliers.
    '''
    def __init__(self) -> None:
        '''
        All items will have access to damages, but most won't use them.
        '''
        self.mutuals = []
        self.enchants = ['MEND', 'UNBR']
        self.damages = ['SHRP', 'SMTE', 'BANE']
    
    def checker(self, desired: list) -> list:
        '''
        Checks if user has input invalid enchantments for the specified item.
        '''
        hmp = defaultdict(list) # Use defaultdict as tool to avoid checking
        for e in desired: 
            hmp[e in self.enchants].append(e) # If one of the input enchantments is invalid, hmp[False]
                                              # will contain the list of invalid enchantments.
        return hmp[False] 
    
    def mutual(self, desired: list) -> bool:
        '''
        Checks if user has input mutually exclusive enchantments for the specified item.
        Returns True if there are conflicting enchantments, False otherwise
        '''
        # Array of counts for different pools
        count = [0] * len(self.mutuals) 
        # Enumerate to get unpack the value and retaining the use of an index
        for idx, li in enumerate(self.mutuals):
            # Loop through the pool of mutually exclusive enchantments
            for e in li:
                if e in desired:
                    count[idx] += 1 # Count how many are present
        for c in count:
            if c > 1:
                return True
        return False
    