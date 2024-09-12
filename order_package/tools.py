from .items import AllPurpose


class Tools(AllPurpose):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(['FORT', 'SILK'])
        self.enchants += ['FORT', 'SILK', 'EFFI']


class Pickaxe(Tools):
    def __init__(self) -> None:
        super().__init__()


class Axe(Tools):
    def __init__(self) -> None:
        super().__init__()
        self.mutuals.append(self.damages)
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