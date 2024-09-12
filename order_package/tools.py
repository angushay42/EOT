from items import AllPurpose


class Tools(AllPurpose):
    def __init__(self) -> None:
        # incompatible: FORT, SILK
        super().__init__()
        self.enchants += ['FORT', 'SILK', 'EFFI']


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


class FishingRod(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.enchants += ['LUCK','LURE']

desired = ['MEND', 'UNBR','IMPL']
x = Pickaxe()
print(x.checker(desired))