from .items import AllPurpose


class Armour(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.protections = ['PROT','BLPR','FIPR','PRPR']
        self.enchants += ['THRN'] + self.protections
        self.mutuals.append(self.protections)

@AllPurpose.register_subclass('Helmet')
class Helmet(Armour):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['RESP','AQUA']

@AllPurpose.register_subclass('Chest')
class Chest(Armour):
    def __init__(self) -> None:
        super().__init__()

@AllPurpose.register_subclass('Leggings')
class Leggings(Armour):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['SWFT']

@AllPurpose.register_subclass('Boots')
class Boots(Armour):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['FRST','DPTH'])
        self.enchants += ['FRST','SOUL','DPTH','FEAT']
    def __repr__(self) -> str:
        return super().__repr__()