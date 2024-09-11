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

class Sword(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += self.damages + ['LOOT', 'FASP', 'KNCK']

class Trident(AllPurpose):
    def __init__(self) -> None:
        # incompatible: Riptide, Channelling
        super().__init__()
        self.enchants += ['IMPL', 'LYAL', 'CHAN', 'RIPT']

class Bow(AllPurpose):
    def __init__(self) -> None:
        # incompatible: INF and ME 
        super().__init__()
        self.enchants += ['FLME','PNCH','POWR','INFI']

class Crossbow(AllPurpose):
    def __init__(self) -> None:
        # incompatible: Piercing, Multi
        super().__init__()
        self.enchants += ['PIER','MLTI','QUIK']

class Mace(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += self.damages + ['BRCH','WIND','DENS','FASP']

class Armour(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['PROT','BLPR','FIPR','PRPR','THRN']

class Helmet(Armour):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['RESP','AQUA']

class Chest(Armour):
    def __init__(self) -> None:
        super().__init__()

class Leggings(Armour):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['SWFT']

class Boots(Armour):
    def __init__(self) -> None:
        # incompatible: Frost Walker, Depth Strider 
        super().__init__()
        self.enchants += ['FRST','SOUL','DPTH','FEAT']

class Tools(AllPurpose):
    def __init__(self) -> None:
        # incompatible: FORT, SILK
        super().__init__()
        self.enchants += ['FORT', 'SILK', 'EFFI']
    
class FishingRod(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['LUCK','LURE']

class Shears(AllPurpose):
    def __init__(self) -> None:
        super().__init__()

class Pickaxe(Tools):
    def __init__(self) -> None:
        super().__init__()

class Axe(Tools):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += self.damages
        
class Hoe(Tools):
    def __init__(self) -> None:
        super().__init__()

class Shovel(Tools):
    def __init__(self) -> None:
        super().__init__()
