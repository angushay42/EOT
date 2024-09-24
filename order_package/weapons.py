from .items import AllPurpose

@AllPurpose.register_subclass('Sword')
class Sword(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(self.damages)
        self.enchants += self.damages + ['LOOT', 'FASP', 'KNCK']

@AllPurpose.register_subclass('Trident')
class Trident(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['CHAN', 'RIPT'])
        self.enchants += ['IMPL', 'LYAL', 'CHAN', 'RIPT']

@AllPurpose.register_subclass('Bow')
class Bow(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['INFI','MEND'])
        self.enchants += ['FLME','PNCH','POWR','INFI']

@AllPurpose.register_subclass('Crossbow')
class Crossbow(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['PIER','MLTI'])
        self.enchants += ['PIER','MLTI','QUIK']

@AllPurpose.register_subclass('Mace')
class Mace(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += self.damages + ['BRCH','WIND','DENS','FASP']
