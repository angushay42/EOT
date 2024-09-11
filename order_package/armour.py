from order_package.items import AllPurpose

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