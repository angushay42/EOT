from .items import AllPurpose

class Sword(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(self.damages)
        self.enchants += self.damages + ['LOOT', 'FASP', 'KNCK']

class Trident(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['CHAN', 'RIPT'])
        self.enchants += ['IMPL', 'LYAL', 'CHAN', 'RIPT']

class Bow(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['INFI','MEND'])
        self.enchants += ['FLME','PNCH','POWR','INFI']

class Crossbow(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['PIER','MLTI'])
        self.enchants += ['PIER','MLTI','QUIK']

class Mace(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += self.damages + ['BRCH','WIND','DENS','FASP']
