from items import AllPurpose

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
