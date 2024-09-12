from .items import AllPurpose

class Armour(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.protections = ['PROT','BLPR','FIPR','PRPR']
        self.enchants += ['THRN'] + self.protections
        self.mutuals.append(self.protections)


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
        super().__init__()
        self.mutuals.append(['FRST','DPTH'])
        self.enchants += ['FRST','SOUL','DPTH','FEAT']